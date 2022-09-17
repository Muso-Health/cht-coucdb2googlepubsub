from models.config.Config import Config
from services.GoogleSecretManager import get_secret_from_secret_manager


class CouchdbAuth:
    username: str
    password: str

    def __init__(self, client):
        CouchdbAuth.username = get_secret_from_secret_manager(client, Config.couchdb_user_secret)
        CouchdbAuth.password = get_secret_from_secret_manager(client, Config.couchdb_password_secret)
