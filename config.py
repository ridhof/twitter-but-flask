"""
This script used to setup the config files that imported from .env
"""
import os


class Config(object):
    """
    Config Object to be used on Flask app.
    """
    DEBUG = os.environ.get("APP_DEBUG")

    BIND = os.environ.get("APP_URL") + ':' + \
        os.environ.get("APP_PORT")
    WORKERS = 2
    WORKER_CONNECTIONS = 1000
    BACKLOG = 64
    TIMEOUT = 30

    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the database we are working with
    # i.e using SQLite
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "DB_TRACK_MODIFICATION")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, os.environ.get("DB_DATABASE"))
    if os.environ.get("DB_CONNECTION") == "mysql":
        if os.environ.get("DB_PASSWORD"):
            SQLALCHEMY_DATABASE_URI = ''.join(
                ('mysql+pymysql://',
                 os.environ.get("DB_USERNAME"),
                 ':',
                 os.environ.get("DB_PASSWORD"),
                 '@',
                 os.environ.get("DB_HOST"),
                 '/',
                 os.environ.get("DB_DATABASE"))
            )
        else:
            SQLALCHEMY_DATABASE_URI = ''.join(
                ('mysql+pymysql://',
                 os.environ.get("DB_USERNAME"),
                 '@',
                 os.environ.get("DB_HOST"),
                 '/',
                 os.environ.get("DB_DATABASE"))
            )

    # Application threads. General assumption is using 2
    # per available processor cores to handle
    # incoming request using one cores and the other is
    # used to performing background operations
    THREADS_PER_PAGE = 2

    # Enable protection against *Cross-Site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolute secret key for data signing
    CSRF_SESSION_KEY = os.environ.get("APP_KEY")
    SECRET_KEY = os.environ.get("APP_KEY")

    LOG_LEVEL = os.environ.get("LOG_LEVEL")
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = 'run.pid'


CONFIG = Config
