from schemas.PredictionResponseSchema import PredictionResponseSchema


class PredictionResponse:
    def __init__(self, prediction_result, generated_text):
        self.prediction_result = prediction_result
        self.generated_text = generated_text

    def serialize(self):
        data_to_serialize = {
            "predicted": {
                "class_name": self.prediction_result["predicted"]["class"],
                "confidence": self.prediction_result["predicted"]["confidence"]
            },
            "probabilities": {
                "probabilities": self.prediction_result["probabilities_dict"]
            },
            "generated_text": self.generated_text
        }

        schema = PredictionResponseSchema()

        return schema.dump(data_to_serialize)
