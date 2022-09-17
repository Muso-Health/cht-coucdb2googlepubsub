from contracts.ConfigService import ConfigService
from models.config.Config import Config


class MockConfigService(ConfigService):
    config: Config

    def store_sequence(self) -> bool:
        return True

    def init(self) -> None:
        self.config = Config()
        self.config.flattening = False
        self.config.url = 'https://muso-mali.app.medicmobile.org'
        self.config.domain = "muso-mali.app.medicmobile.org"
        self.config.protocol = "https"
        self.config.batch_size = 20000
        self.config.last_couchdb_sequence = None
        self.config.sleep_seconds = 120

    def get_pub_sub_topic(self, form_id: str, version: str) -> str:
        return 'couchdb-changes-test'

