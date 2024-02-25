import requests
from marshmallow import Schema, fields, validate, validates, ValidationError
from constants.ModelsConstants import ModelsConstants

models_constant = ModelsConstants()


class PredictionRequestSchema(Schema):
    model_type = fields.String(required=True, validate=validate.OneOf(models_constant.available_models))
    content_url = fields.Url(required=True)

    @validates("content_url")
    def validate_url(self, value: str):
        if not value.startswith(models_constant.cloud_storage_url_prefix):
            raise ValidationError("URL does not have the expected prefix.")

        try:
            response = requests.head(value)

            if response.status_code != 200:
                raise ValidationError("URL is not reachable")
        except requests.RequestException:
            raise ValidationError("URL is not valid or not reachable")
