from typing import Any

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from models.config import Config

# Cloud SQL ORM
Base = declarative_base()


class CloudConfig(Base):
    __tablename__ = 'configs'
    id = Column(Integer, primary_key=True)

    flattening = Column(Boolean, nullable=False, default=False)
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
    old_accepted = Column(Boolean, nullable=False, default=False)

    def __init__(self,
                 flattening: bool,
                 url: str,
                 domain: str,
                 protocol: str,
                 batch_size: str,
                 last_couchdb_sequence: str,
                 sleep_seconds: str,
                 couchdb_user_secret: str,
                 couchdb_password_secret: str,
                 instance_type: str,
                 country_code: str,
                 old_accepted: bool,
                 *args: Any, **kwargs: Any
                 ):
        super().__init__(*args, **kwargs)
        self.flattening = flattening
        self.url = url
        self.domain = domain,
        self.protocol = protocol,
        self.batch_size = batch_size
        self.last_couchdb_sequence = last_couchdb_sequence
        self.sleep_seconds = sleep_seconds
        self.couchdb_user_secret = couchdb_user_secret
        self.couchdb_password_secret = couchdb_password_secret,
        self.instance_type = instance_type,
        self.country_code = country_code
        self.old_accepted = old_accepted
