from typing import Any

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from models.config import Config

# Cloud SQL ORM
Base = declarative_base()


class CloudConfig(Base):
    __tablename__ = 'configs'
    id = Column(Integer, primary_key=True)

    flattening = Column(Boolean, nullable=False, default=True)
    url = Column(String)
    domain = Column(String)
    protocol = Column(String)
    batch_size = Column(Integer)
    last_couchdb_sequence = Column(String)
    sleep_seconds = Column(Integer)
    couchdb_user_secret = Column(String)
    couchdb_password_secret = Column(String)
    instance_type = Column(String)
    country_code = Column(String)

    def __init__(self,
                 config: Config,
                 *args: Any, **kwargs: Any
                 ):
        super().__init__(*args, **kwargs)
        self.flattening = config.flattening
        self.url = config.url
        self.domain = config.domain,
        self.protocol = config.protocol,
        self.batch_size = config.batch_size
        self.last_couchdb_sequence = config.last_couchdb_sequence
        self.sleep_seconds = config.sleep_seconds
        self.couchdb_user_secret = config.couchdb_user_secret
        self.couchdb_password_secret = config.couchdb_password_secret,
        self.instance_type = config.instance_type,
        self.country_code = config.country_code
