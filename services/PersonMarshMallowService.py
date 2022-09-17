from marshmallow import Schema, fields, ValidationError, EXCLUDE

from contracts.SchemaService import SchemaService


class PersonSchema(Schema):
    _id = fields.Str(required=True)
    _rev = fields.Str(required=True)
    type = fields.Str(required=True)
    reported_date = fields.Integer(required=True)


class PersonMarshMallowService(SchemaService):
    def __init__(self):
        self.schema = PersonSchema()

    def validate_json(self, json_dict: dict) -> bool:
        try:
            validated = self.schema.load(json_dict, unknown=EXCLUDE)
            return validated and json_dict['type'] == 'person'
        except ValidationError:
            print(ValidationError.messages_dict)
            return False
