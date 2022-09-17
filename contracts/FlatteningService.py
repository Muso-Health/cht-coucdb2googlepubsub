from abc import ABC


class FlatteningService(ABC):

    def flatten(self, json_dict: dict, services: list = None) -> dict:
        pass
