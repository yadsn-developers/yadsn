"""
Scripts.
"""

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from yadsn.app import create_app
from yadsn.catalogs import Resources


app = create_app()
manager = Manager(app)

migrate = Migrate(app, Resources.database())
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
