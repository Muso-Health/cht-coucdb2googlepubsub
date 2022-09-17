from contracts.ConfigService import ConfigService
from contracts.FlatteningService import FlatteningService
from contracts.PubSubService import PubSubService
from contracts.SchemaService import SchemaService


class CouchdbDoc:
    def __init__(self,
                 schema: SchemaService,
                 sub_pub: PubSubService,
                 flatter: FlatteningService = None
                 ):
        self.schema = schema
        self.flatter = flatter
        self.sub_pub = sub_pub

    def is_valid_doc(self, json_dict: dict) -> bool:
        return self.schema.validate_json(json_dict)

    def flatten(self, json_dict, schemas: list = None) -> dict:
        if self.flatter is not  None:
            return self.flatter.flatten(json_dict, schemas)
        return json_dict

    def dispatch_to_pub_sub(self, topic: str, data: dict) -> str:
        return self.sub_pub.dispatch_to_pub_sub(topic, data)
