import requests
from marshmallow import Schema, fields, validate, validates, ValidationError
from constants.ModelsConstants import ModelsConstants

class PredictionRequestSchema(Schema):
    model_type = fields.String(required=True, validate=validate.OneOf(ModelsConstants().available_models))
    content_url = fields.Url(required=True)

    @validates("content_url")
    def validate_url(self, value):
        try:
            response = requests.head(value)

            if response.status_code != 200:
                raise ValidationError("URL is not reachable")
        except requests.RequestException:
            raise ValidationError("URL is not valid or not reachable")
