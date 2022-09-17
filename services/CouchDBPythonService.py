from couchdb import Server, Unauthorized
from contracts.CouchdbChangesHttpService import CouchdbChangesHttpService
from models.couchdb_request.CouchdbAuth import CouchdbAuth
from models.couchdb_request.CouchdbRequest import CouchdbRequest
from models.couchdb_request.CouchdbResponse import CouchdbResponse


class CouchDBPythonService(CouchdbChangesHttpService):
    def get_batch(self, request_config: CouchdbRequest, auth: CouchdbAuth) -> CouchdbResponse:
        url = f"{request_config.protocol}://{auth.username}:{auth.password}@{request_config.domain}"
        server = Server(url)
        response = CouchdbResponse()
        try:
            db = server['medic']
            print("authorized")
            if request_config.since is None:
                changes = db.changes(include_docs=True, since=0, limit=request_config.limit)
            else:
                changes = db.changes(include_docs=True, since=request_config.since, limit=request_config.limit)
            response.last_sequence_number = changes["last_seq"]
            response.pending = changes["pending"]
            response.docs = changes["results"]
        except Unauthorized:
            print("unauthorized")
            response.pending = -1
            response.last_sequence_number = None
            response.docs = []

        return response

