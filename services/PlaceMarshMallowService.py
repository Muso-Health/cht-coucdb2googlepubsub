from marshmallow import Schema, fields, ValidationError, EXCLUDE

from contracts.SchemaService import SchemaService


class PlaceSchema(Schema):
    _id = fields.Str(required=True)
    _rev = fields.Str(required=True)
    type = fields.Str(required=True)
    contact_type = fields.Str(required=True)
    reported_date = fields.Integer(required=True)


class PlaceMarshMallowService(SchemaService):
    def __init__(self):
        self.schema = PlaceSchema()

    def validate_json(self, json_dict: dict) -> bool:
        try:
            validated = self.schema.load(json_dict, unknown=EXCLUDE)
            return validated and json_dict['type'] == 'contact' and json_dict['contact_type'] in [
                'c50_family', 'c40_chw_area', 'c30_supervisor_area', 'c20_health_area', 'c10_site'
            ]
        except ValidationError:
            print(ValidationError.messages_dict)
            return False

