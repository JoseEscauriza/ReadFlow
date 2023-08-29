from .util import ROOT_DIR
import environ
import psycopg2 as pg

# create environ connection
env = environ.Env()

# set enviroment path
environ.Env.read_env(str(ROOT_DIR / ".env"))


class Database():
    """This is a singleton class, it is used for database connection and query execution.
    """

    _instance = None

    def __new__(cls):
        if Database._instance is None:
            Database._instance = super().__new__(cls)
            Database._instance.__init__()

        return Database._instance._conn

    def __init__(self) -> None:
        self._conn = pg.connect(
            host=env.str("DB_HOST"),
            port=env.str("DB_PORT"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASS"),
            dbname=env.str("DB_NAME")
        )
