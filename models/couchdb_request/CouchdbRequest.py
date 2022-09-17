from models.config.Config import Config


class CouchdbRequest:
    server_url: str
    protocol: str
    domain: str
    since: str
    limit: int
    api_url: str

    def __init__(self, config: Config):
        self.protocol = config.protocol
        self.domain = config.domain
        self.server_url = f"{config.protocol}://{config.domain}"
        self.since = config.last_couchdb_sequence
        self.limit = config.batch_size
        if self.since is not None:
            self.api_url = f"{self.server_url}/_changes?include_docssince={self.since}&limit={self.limit}"
        else:
            self.api_url = f"{self.server_url}/_changes?limit={self.limit}"

