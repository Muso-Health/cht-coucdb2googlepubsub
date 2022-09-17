from abc import ABC


class SchemaService(ABC):

    def validate_json(self, json_dict: dict) -> bool:
        pass
