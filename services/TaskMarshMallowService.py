from datetime import datetime

from marshmallow import Schema, fields, ValidationError, EXCLUDE

from contracts.SchemaService import SchemaService


class TaskSchema(Schema):
    _id = fields.Str(required=True)
    _rev = fields.Str(required=True)
    type = fields.Str(required=True)
    user = fields.Str(required=True)
    owner = fields.Str(required=True)
    state = fields.Str(required=True)
    emission = fields.Dict(required=True)


class TaskEmissionSchema(Schema):
    title = fields.Str(required=True)
    startDate = fields.Date(required=True)
    endDate = fields.Date(required=True)
    dueDate = fields.Date(required=True)


class TaskMarshMallowService(SchemaService):
    def __init__(self):
        self.schema = TaskSchema()
        self.emission_schema = TaskEmissionSchema()

    def validate_json(self, json_dict: dict) -> bool:
        try:
            validated = self.schema.load(json_dict, unknown=EXCLUDE)
            emission_validated = self.validate_emission(json_dict['emission'])
            return validated and emission_validated and json_dict['type'] != 'task'
        except ValidationError:
            print(ValidationError.messages_dict)
            return False

    def validate_emission(self, json_dict: dict):
        try:
            validated = self.emission_schema.load(json_dict, unknown=EXCLUDE)
            if not validated:
                return False
            try:
                due_date = datetime.strptime(json_dict['dueDate'], '%Y-%m-%d').date()
                if not due_date:
                    return False
                if due_date.year != datetime.now().year:
                    return False
                return True
            except ValueError:
                return False
        except ValidationError:
            print(ValidationError.messages_dict)
            return False
