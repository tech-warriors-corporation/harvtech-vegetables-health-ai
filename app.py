import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

from constants.ModelsConstants import security_constants_instance
from gemini.gemini import Gemini
from logs.log_config import configure_logger
from prediction_requests.PredictionRequest import PredictionRequest
from responses.PredictionResponse import PredictionResponse
from services.PredictionService import PredictionService

logger = configure_logger(__name__)
app = Flask(__name__)
cors = CORS(app)  # TODO: adicionar origin apenas para aplicação do Node.
prediction_service = PredictionService()


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    try:
        prediction_request = PredictionRequest(data)
        validated_data = prediction_request.load()
        
        model = validated_data["model_type"]
        content_url = validated_data["content_url"]
        image_content = prediction_service.get_image(content_url)
        prediction = prediction_service.predict_image(model, image_content)
        generated_text = Gemini().generate_text(predicted=prediction['predicted'], model_type=model)
        response = PredictionResponse(prediction_result=prediction, generated_text=generated_text)

         
        return jsonify(response.serialize())
    except ValueError as error:
        logger.error(f"An error occurred during validation: {error}")

        return jsonify({"error": str(error)}), 400
    except requests.RequestException as error:
        logger.error(f"Failed to retrieve the image from the URL: {error}")

        return jsonify({"error": "Failed to retrieve the image from the URL"}), 400

    except IOError as e:
        logger.error(f"Error while trying to read file: {e}")

        return jsonify({"error": "Error while trying to read file"}), 500
    except Exception as error:
        logger.error(f"An error occurred during prediction: {error}")

        return jsonify({"error": "An error occurred during prediction"}), 500


if __name__ == "__main__":
    if security_constants_instance.flask_env == 'production':
         app.run(host='0.0.0.0', debug=False, port=security_constants_instance.flask_port, ssl_context=(security_constants_instance.cert, security_constants_instance.key))
    else:
        app.run(host='0.0.0.0', debug=True, port=security_constants_instance.flask_port)
    
