"""
Module to run the Flask app.
"""
import logging.handlers
from abc import ABC

from dotenv import load_dotenv
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gunicorn.app.base import BaseApplication
from six import iteritems

from app import create_app, DB as db
load_dotenv(override=True)

from config import CONFIG as config
app = create_app(config)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class StandaloneApplication(BaseApplication, ABC):
    def __init__(self, application, options):
        self.application = application
        self.options = options or {}
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(
            self.options) if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


@manager.command
def run():
    """
    To run, use: python manager.py run
    """
    app.logger.setLevel(app.config.get('LOG_LEVEL', logging.INFO))
    service_config = {
        'bind': app.config.get('BIND', '0.0.0.0:8080'),
        'workers': app.config.get('WORKERS', 1 * 2 + 1),
        'worker_connections': app.config.get('WORKER_CONNECTIONS', 10000),
        'backlog': app.config.get('BACKLOG', 2048),
        'timeout': app.config.get('TIMEOUT', 60),
        'loglevel': app.config.get('LOG_LEVEL', 'info'),
        'pidfile': app.config.get('PID_FILE', 'run.pid'),
        'sqlalchemy_track_modifications': app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS', False),
    }
    StandaloneApplication(app, service_config).run()


@manager.command
def debug():
    """
    to run, use: python manager.py debug
    """
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
