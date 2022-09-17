from typing import Any

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

from models.BatchInfo import BatchInfo

# Cloud SQL ORM
Base = declarative_base()


class BatchStat(Base):
    __tablename__ = 'batch_infos'
    id = Column(Integer, primary_key=True)

    batch_id = Column(Integer)
    instance = Column(String)
    start = Column(TIMESTAMP)
    end = Column(TIMESTAMP)
    received = Column(Integer)
    received_forms = Column(Integer)
    validated_forms = Column(Integer)
    malformed_forms = Column(Integer)
    flatten_forms = Column(Integer)
    pending = Column(Integer)
    start_seq = Column(String)
    end_seq = Column(String)

    def __init__(self,
                 batch_info: BatchInfo,
                 *args: Any, **kwargs: Any
                 ):
        super().__init__(*args, **kwargs)
        self.batch_id = batch_info.batch_id
        self.instance = batch_info.instance
        self.start = batch_info.start
        self.end = batch_info.end
        self.received = batch_info.received
        self.received_forms = batch_info.received_forms
        self.validated_forms = batch_info.validated_forms
        self.malformed_forms = batch_info.malformed_forms
        self.flatten_forms = batch_info.flatten_forms
        self.uniques_id = batch_info.pending
        self.start_seq = batch_info.start_seq
        self.end_seq = batch_info.end_seq
