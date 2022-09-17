from abc import ABC

from models.couchdb_request.CouchdbAuth import CouchdbAuth
from models.couchdb_request.CouchdbRequest import CouchdbRequest
from models.couchdb_request.CouchdbResponse import CouchdbResponse


class CouchdbChangesHttpService(ABC):
    def get_batch(self, request_config: CouchdbRequest, auth: CouchdbAuth) -> CouchdbResponse:
        pass
