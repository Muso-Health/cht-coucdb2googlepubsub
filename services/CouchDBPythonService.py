from couchdb import Server, Unauthorized
from contracts.CouchdbChangesHttpService import CouchdbChangesHttpService
from models.couchdb_request.CouchdbAuth import CouchdbAuth
from models.couchdb_request.CouchdbRequest import CouchdbRequest
from models.couchdb_request.CouchdbResponse import CouchdbResponse


class CouchDBPythonService(CouchdbChangesHttpService):
    def get_batch(self, options: dict = None) -> CouchdbResponse:
        url = f"{CouchdbRequest.protocol}://{CouchdbAuth.username}:{CouchdbAuth.password}@{CouchdbRequest.domain}"
        server = Server(url)
        try:
            db = server['medic']
            print("authorized")
            if CouchdbRequest.since is None:
                changes = db.changes(include_docs=True, since=0, limit=CouchdbRequest.limit)
            else:
                changes = db.changes(include_docs=True, since=CouchdbRequest.since, limit=CouchdbRequest.limit)
            CouchdbResponse.last_sequence_number = changes["last_seq"]
            CouchdbResponse.pending = changes["pending"]
            CouchdbResponse.docs = changes["results"]
        except Unauthorized:
            print("unauthorized")
            CouchdbResponse.pending = -1
            CouchdbResponse.last_sequence_number = None
            CouchdbResponse.docs = []

        return CouchdbResponse()

