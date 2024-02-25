import requests
from io import BytesIO
from factories.ModelFactory import ModelFactory

class PredictionService:
    @staticmethod
    def get_image(url):
        response = requests.get(url)

        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise ValueError("Failed to retrieve the image from the URL")

    @staticmethod
    def predict_image(model_type, image_content):
        model = ModelFactory.get_model(model_type)

        if not model:
            raise ValueError("Model type not supported")

        return model.predict(image_content=image_content)
