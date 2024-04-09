from schemas.PredictionRequestSchema import PredictionRequestSchema


class PredictionRequest:
    def __init__(self, data):
        self.data = data

    def validate(self):
        schema = PredictionRequestSchema()
        errors = schema.validate(self.data)

        if errors:
            raise ValueError(errors)

        return True

    def load(self):
        if self.validate():
            schema = PredictionRequestSchema()

            return schema.load(self.data)
