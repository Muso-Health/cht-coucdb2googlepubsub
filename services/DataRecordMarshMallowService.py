from marshmallow import Schema, fields, ValidationError, EXCLUDE

from contracts.SchemaService import SchemaService


class DataRecordSchema(Schema):
    _id = fields.Str(required=True)
    _rev = fields.Str(required=True)
    form = fields.Str(required=True)
    type = fields.Str(required=True)
    # version = fields.Str(required=True)
    reported_date = fields.Integer(required=True)
    fields = fields.Dict(required=True)


class DataRecordMarshMallowService(SchemaService):
    def __init__(self):
        self.schema = DataRecordSchema()

    def validate_json(self, json_dict: dict) -> bool:
        try:
            validated = self.schema.load(json_dict, unknown=EXCLUDE)
            return validated
        except ValidationError:
            print(ValidationError.messages_dict)
            return False
