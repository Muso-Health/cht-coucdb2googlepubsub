from models.config.Config import Config


class CouchdbRequest:
    server_url: str
    protocol: str
    domain: str
    since: str
    limit: int
    api_url: str

    def __init__(self):
        self.protocol = Config.protocol
        self.domain = Config.domain
        self.server_url = f"{Config.protocol}://{Config.domain}"
        self.since = Config.last_couchdb_sequence
        self.limit = Config.batch_size
        if self.since is not None:
            self.api_url = f"{self.server_url}/_changes?include_docssince={self.since}&limit={self.limit}"
        else:
            self.api_url = f"{self.server_url}/_changes?limit={self.limit}"

