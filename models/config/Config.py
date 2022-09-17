def to_string():
    return f"""
    url: {Config.url},
    protocol: {Config.protocol},
    domain: {Config.domain},
    country_code: {Config.country_code},
    instance_type: {Config.instance_type},
    last_couchdb_sequence: {Config.last_couchdb_sequence},
    sleep_seconds: {Config.sleep_seconds},
    batch_size: {Config.batch_size},
    flattening; {Config.flattening},
    couchdb_user_secret: {Config.couchdb_user_secret},
    couchd_password_secret: {Config.couchdb_password_secret}
    """


class Config:
    url: str
    protocol: str
    domain: str
    country_code: str
    instance_type: str
    last_couchdb_sequence: str
    sleep_seconds: int
    batch_size: int
    flattening: bool
    couchdb_user_secret: str
    couchdb_password_secret: str

