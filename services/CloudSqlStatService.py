from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from contracts.StatService import StatService
from services.cloud_sql.ORM.BatchStat import BatchStat
from models.BatchInfo import BatchInfo


class CloudSqlStatService(StatService):
    def __init__(self, db):
        self.db = db

    def publish_batch_stat(self, info: BatchInfo):
        if self.db is not None:
            session = Session(self.db)
            stat = BatchStat(
                batch_id=info.batch_id,
                instance=info.instance,
                start_at=info.start_at,
                end_at=info.end_at,
                received=info.received,
                received_forms=info.received_forms,
                validated_forms=info.validated_forms,
                validated_persons=info.validated_persons,
                validated_places=info.validated_places,
                validated_tasks=info.validated_tasks,
                malformed_forms=info.malformed_forms,
                flatten_forms=info.flatten_forms,
                pending=info.pending,
                start_seq=info.start_seq,
                end_seq=info.end_seq
            )
            session.add(stat)
            session.commit()
            session.close()

    def verify_connexion(self) -> bool:
        try:
            self.db.connect()
            return True
        except SQLAlchemyError as err:
            return False
