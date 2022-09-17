import os
from services.GoogleSecretManager import get_secret_from_secret_manager
from google.cloud.secretmanager_v1 import SecretManagerServiceClient
import sqlalchemy


def connect_to_cloud_server(client: SecretManagerServiceClient):
    db_config = {
        # [START cloud_sql_postgres_sqlalchemy_limit]
        # Pool size is the maximum number of permanent connections to keep.
        "pool_size": 5,
        # Temporarily exceeds the set pool_size if no connections are available.
        "max_overflow": 2,
        # The total number of concurrent connections for your application will be
        # a total of pool_size and max_overflow.
        # [END cloud_sql_postgres_sqlalchemy_limit]

        # [START cloud_sql_postgres_sqlalchemy_backoff]
        # SQLAlchemy automatically uses delays between failed connection attempts,
        # but provides no arguments for configuration.
        # [END cloud_sql_postgres_sqlalchemy_backoff]

        # [START cloud_sql_postgres_sqlalchemy_timeout]
        # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
        # new connection from the pool. After the specified amount of time, an
        # exception will be thrown.
        "pool_timeout": 30,  # 30 seconds
        # [END cloud_sql_postgres_sqlalchemy_timeout]

        # [START cloud_sql_postgres_sqlalchemy_lifetime]
        # 'pool_recycle' is the maximum number of seconds a connection can persist.
        # Connections that live longer than the specified amount of time will be
        # reestablished
        "pool_recycle": 1800,  # 30 minutes
        # [END cloud_sql_postgres_sqlalchemy_lifetime]
    }
    return init_unix_connection_engine_to_cloud_sql(db_config, client)


def init_unix_connection_engine_to_cloud_sql(db_config, client):
    # [START cloud_sql_postgres_sqlalchemy_create_socket]
    # Remember - storing secrets in plaintext is potentially unsafe. Consider using
    # something like https://cloud.google.com/secret-manager/docs/overview to help keep
    # secrets secret.

    cloud_sql_pass = get_secret_from_secret_manager(client, 'cloud-sql-test-admin-password')
    cloud_sql_user = 'postgres'
    db_name = 'mali-prod-couchdb2pubsub'
    project = 'musohealth'
    region = 'us-central1'
    instance = 'test'
    db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
    instance_connection_name = f"{project}:{region}:{instance}"

    pool = sqlalchemy.create_engine(

        # Equivalent URL:
        # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
        #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
        # Note: Some drivers require the `unix_sock` query parameter to use a different key.
        # For example, 'psycopg2' uses the path set to `host` in order to connect successfully.
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=cloud_sql_user,  # e.g. "my-database-user"
            password=cloud_sql_pass,  # e.g. "my-database-password"
            database=db_name,  # e.g. "my-database-name"
            query={
                "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                    db_socket_dir,  # e.g. "/cloudsql"
                    instance_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        ),
        **db_config
    )
    # [END cloud_sql_postgres_sqlalchemy_create_socket]
    pool.dialect.description_encoding = None
    return pool
