from schemas.PredictionResponseSchema import PredictionResponseSchema

class PredictionResponse:
    def __init__(self, prediction_result):
        self.prediction_result = prediction_result

    def serialize(self):
        data_to_serialize = {
            "predicted": {
                "class_name": self.prediction_result["predicted"]["class"],
                "confidence": self.prediction_result["predicted"]["confidence"]
            },
            "probabilities": {
                "probabilities": self.prediction_result["probabilities_dict"]
            }
        }

        schema = PredictionResponseSchema()

        return schema.dump(data_to_serialize)
