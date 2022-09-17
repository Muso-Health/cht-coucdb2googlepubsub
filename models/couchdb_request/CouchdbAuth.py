from services.GoogleSecretManager import get_secret_from_secret_manager


class CouchdbAuth:
    username: str
    password: str

    def __init__(self, client, username_secret: str, password_secret: str):
        self.username = get_secret_from_secret_manager(client, username_secret)
        self.password = get_secret_from_secret_manager(client, password_secret)
