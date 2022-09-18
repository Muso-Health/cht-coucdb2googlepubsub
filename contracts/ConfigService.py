from abc import ABC


from models.config.Config import Config


class ConfigService(ABC):

    def store_sequence(self) -> bool:
        pass

    def init(self) -> bool:
        pass

    def update(self):
        pass
