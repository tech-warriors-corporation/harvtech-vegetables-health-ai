from marshmallow import Schema, fields


class PredictionDetailsSchema(Schema):
    class Meta:
        ordered = True

    class_name = fields.Str(required=True)
    confidence = fields.Float(required=True)


class ProbabilitiesSchema(Schema):
    class Meta:
        ordered = True

    probabilities = fields.Dict(keys=fields.Str(), values=fields.Float())


class PredictionResponseSchema(Schema):
    predicted = fields.Nested(PredictionDetailsSchema, required=True)
    probabilities = fields.Nested(ProbabilitiesSchema, required=True)
