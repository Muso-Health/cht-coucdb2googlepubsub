from sqlalchemy.orm import Session
from sqlalchemy import update

from contracts.ConfigService import ConfigService
from models.config.Config import Config
from services.cloud_sql.ORM.CloudConfig import CloudConfig


class CloudSqlConfigService(ConfigService):
    config: Config

    def __init__(self, db):
        self.db = db

    def store_sequence(self) -> bool:
        self.update()
        return True

    def init(self) -> bool:
        if self.db is not None:
            session = Session(self.db)
            cloud_config = session.get(CloudConfig, 1)
            if cloud_config is None:
                return False

            self.config.flattening = cloud_config.flattening
            self.config.url = cloud_config.url
            self.config.domain = cloud_config.domain
            self.config.batch_size = cloud_config.batch_size
            self.config.last_couchdb_sequence = cloud_config.last_couchdb_sequence
            self.config.sleep_seconds = cloud_config.sleep_seconds
            return True

    def update(self):
        if self.db is not None:
            session = Session(self.db)
            session.execute(
                update(CloudConfig).
                where(CloudConfig.id == 1).
                values(last_couchdb_sequence=self.config.last_couchdb_sequence)
            )
