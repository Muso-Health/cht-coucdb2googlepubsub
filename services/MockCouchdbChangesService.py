from contracts.CouchdbChangesHttpService import CouchdbChangesHttpService
from models.couchdb_request.CouchdbAuth import CouchdbAuth
from models.couchdb_request.CouchdbRequest import CouchdbRequest
from models.couchdb_request.CouchdbResponse import CouchdbResponse


class MockCouchdbChangesService(CouchdbChangesHttpService):

    def get_batch(self, request_config: CouchdbRequest, auth: CouchdbAuth) -> CouchdbResponse:
        data = CouchdbResponse()
        data.last_sequence_number = '325-qsdqsdqsd'
        data.docs = [
            {
                "type": "data_record",
                "form": "anc_followup",
                "_id": "qsdqsd",
                "_rev": "5-qsdqsd",
                "reported_date": 165658785,
                "version": 'v2',
                "fields": {
                    "data": {
                        "age": 54,
                        "sex": "male"
                    },

                    "sata": {
                        "au": "gold",
                        "age": 54,
                        "sex": "male"
                    }
                }
            },
            {
                "type": "contact",
                "_id": "qsdqsd",
                "_rev": "5-qsdqsd",
                "contact_type": "c40_chw_area",
                "version": 'new'
            },
            {
                "type": "info",
                "_id": "qsdqsd",
                "_rev": "5-qsdqsd"
            }
        ]
        return data
