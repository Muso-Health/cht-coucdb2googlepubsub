from typing import Any

from sqlalchemy import Column, Integer, String, Boolean

from models.config import Config


class CloudConfig:
    __tablename__ = 'configs'
    id = Column(Integer, primary_key=True)

    flattening = Column(Boolean, nullable=False, default=True)
    url = Column(String)
    domain = Column(String)
    protocol = Column(String)
    batch_size = Column(Integer)
    last_couchdb_sequence = Column(String)
    sleep_seconds = Column(Integer)

    def __init__(self,
                 config: Config,
                 *args: Any, **kwargs: Any
                 ):
        super().__init__(*args, **kwargs)
        self.flattening = config.flattening
        self.url = config.url
        self.domain = config.domain
        self.batch_size = config.batch_size
        self.last_couchdb_sequence = config.last_couchdb_sequence
        self.sleep_seconds = config.sleep_seconds
