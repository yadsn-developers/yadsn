"""
Scripts.
"""

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, sqlalchemy


migrate = Migrate(app, sqlalchemy)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
