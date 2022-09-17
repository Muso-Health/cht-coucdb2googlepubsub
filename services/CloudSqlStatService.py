from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from contracts.StatService import StatService
from services.cloud_sql.ORM.BatchStat import BatchStat
from models import BatchInfo


class CloudSqlStatService(StatService):
    def __init__(self, db):
        self.db = db

    def publish_batch_stat(self, info: BatchInfo):
        if self.db is not None:
            session = Session(self.db)
            session.add(BatchStat(info))
            session.commit()
            session.close()

    def verify_connexion(self) -> bool:
        try:
            self.db.connect()
            return True
        except SQLAlchemyError as err:
            return False
