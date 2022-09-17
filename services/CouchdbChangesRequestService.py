import requests
from requests.auth import HTTPBasicAuth

from contracts.CouchdbChangesHttpService import CouchdbChangesHttpService
from models.couchdb_request.CouchdbAuth import CouchdbAuth
from models.couchdb_request.CouchdbRequest import CouchdbRequest
from models.couchdb_request.CouchdbResponse import CouchdbResponse


class CouchdbChangesRequestService(CouchdbChangesHttpService):
    def get_batch(self, request_config: CouchdbRequest, auth: CouchdbAuth) -> CouchdbResponse:
        response = requests.get(request_config.api_url, verify=False, auth=HTTPBasicAuth(auth.username, auth.password))
        if response.status_code == 200:
            data = response.content

        else:
            result = CouchdbResponse()
            result.last_sequence_number = None
            result.docs = []
            return result
