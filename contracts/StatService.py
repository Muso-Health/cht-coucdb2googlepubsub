from abc import ABC

from models import BatchInfo


class StatService(ABC):
    def publish_batch_stat(self, info: BatchInfo):
        pass
