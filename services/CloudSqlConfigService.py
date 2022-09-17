from sqlalchemy.orm import Session
from sqlalchemy import update

from contracts.ConfigService import ConfigService
from models.config.Config import Config
from services.cloud_sql.ORM.CloudConfig import CloudConfig


class CloudSqlConfigService(ConfigService):
    config: Config = Config()

    def __init__(self, db):
        self.db = db

    def store_sequence(self) -> bool:
        self.update()
        return True

    def init(self) -> bool:
        if self.db is not None:
            session = Session(self.db)
            cloud_config = session.query(CloudConfig).get(1)
            if cloud_config is None:
                return False

            CloudSqlConfigService.config.flattening = cloud_config.flattening
            CloudSqlConfigService.config.url = cloud_config.url
            CloudSqlConfigService.config.domain = cloud_config.domain
            CloudSqlConfigService.config.batch_size = cloud_config.batch_size
            CloudSqlConfigService.config.last_couchdb_sequence = cloud_config.last_couchdb_sequence
            CloudSqlConfigService.config.sleep_seconds = cloud_config.sleep_seconds
            CloudSqlConfigService.config.couchdb_user_secret = cloud_config.couchdb_user_secret
            CloudSqlConfigService.config.couchdb_password_secret = cloud_config.couchdb_password_secret
            CloudSqlConfigService.config.instance_type = cloud_config.instance_type
            CloudSqlConfigService.config.country_code = cloud_config.country_code
            return True

    def update(self):
        if self.db is not None:
            session = Session(self.db)
            session.execute(
                update(CloudConfig).
                where(CloudConfig.id == 1).
                values(last_couchdb_sequence=CloudSqlConfigService.config.last_couchdb_sequence)
            )
