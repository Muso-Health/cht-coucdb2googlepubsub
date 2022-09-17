from models.config.Config import Config


class CouchdbRequest:
    server_url: str
    protocol: str
    domain: str
    since: str
    limit: int
    api_url: str

    def __init__(self):
        CouchdbRequest.protocol = Config.protocol
        CouchdbRequest.domain = Config.domain
        CouchdbRequest.server_url = f"{Config.protocol}://{Config.domain}"
        CouchdbRequest.since = Config.last_couchdb_sequence
        CouchdbRequest.limit = Config.batch_size
        if CouchdbRequest.since is not None:
            CouchdbRequest.api_url = f"{CouchdbRequest.server_url}/_changes?include_docssince={CouchdbRequest.since}&limit={CouchdbRequest.limit}"
        else:
            CouchdbRequest.api_url = f"{CouchdbRequest.server_url}/_changes?limit={CouchdbRequest.limit}"

