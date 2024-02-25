import requests
from flask import Flask, jsonify, request
from prediction_requests.PredictionRequest import PredictionRequest
from responses.PredictionResponse import PredictionResponse
from services.PredictionService import PredictionService
from logs.log_config import configure_logger

logger = configure_logger(__name__)
app = Flask(__name__)
prediction_service = PredictionService()

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.json

    try:
        prediction_request = PredictionRequest(data)
        validated_data = prediction_request.load()
        model = validated_data["model_type"]
        content_url = validated_data["content_url"]
        image_content = prediction_service.get_image(content_url)
        prediction = prediction_service.predict_image(model, image_content)
        response = PredictionResponse(prediction_result=prediction)

        return jsonify(response.serialize())
    except ValueError as error:
        logger.error(f"An error occurred during validation: {error}")

        return jsonify({ "error": str(error) }), 400
    except requests.RequestException as error:
        logger.error(f"Failed to retrieve the image from the URL: {error}")

        return jsonify({ "error": "Failed to retrieve the image from the URL" }), 400
    except Exception as error:
        logger.error(f"An error occurred during prediction: {error}")

        return jsonify({ "error": "An error occurred during prediction" }), 500

if __name__ == "__main__":
    app.run(debug=True)
