from datetime import datetime
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
    start_at = Column(TIMESTAMP)
    end_at = Column(TIMESTAMP)
    received = Column(Integer)
    received_forms = Column(Integer)
    validated_forms = Column(Integer)
    validated_persons = Column(Integer)
    validated_places = Column(Integer)
    validated_tasks = Column(Integer)
    validated_form_def = Column(Integer)
    malformed_forms = Column(Integer)
    flatten_forms = Column(Integer)
    pending = Column(Integer)
    start_seq = Column(String)
    end_seq = Column(String)

    def __init__(self,
                 batch_id: int,
                 instance: str,
                 start_at: datetime,
                 end_at: datetime,
                 received: int,
                 received_forms: int,
                 validated_forms: int,
                 validated_persons: int,
                 validated_places: int,
                 validated_tasks: int,
                 validated_form_def: int,
                 malformed_forms: int,
                 flatten_forms: int,
                 pending: int,
                 start_seq: str,
                 end_seq: str,
                 *args: Any, **kwargs: Any
                 ):
        super().__init__(*args, **kwargs)
        self.batch_id = batch_id
        self.instance = instance
        self.start_at = start_at
        self.end_at = end_at
        self.received = received
        self.received_forms = received_forms
        self.validated_forms = validated_forms
        self.validated_persons = validated_persons
        self.validated_places = validated_places
        self.validated_tasks = validated_tasks
        self.validated_form_def = validated_form_def
        self.malformed_forms = malformed_forms
        self.flatten_forms = flatten_forms
        self.pending = pending
        self.start_seq = start_seq
        self.end_seq = end_seq
