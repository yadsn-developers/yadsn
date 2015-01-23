"""
YADSN Flask Web Application.
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../extra/yadsn/'))

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from objects import AbstractCatalog
from objects.providers import Singleton
from objects.injections import InitArg

from yadsn import YADSN, YADSNModels, YADSNDependencies


class Catalog(AbstractCatalog):
    """
    Objects catalog.
    """

    db = Singleton(create_engine,
                   InitArg('name_or_url', 'sqlite:///db.sqlite'))
    """ :type: (objects.Provider) -> sqlalchemy.engine.interfaces.Connectable """

    session = Singleton(Session,
                        InitArg('bind', db))
    """ :type: (objects.Provider) -> sqlalchemy.orm.Session """


YADSNDependencies.database.satisfy(Catalog.db)
YADSNDependencies.database_session.satisfy(Catalog.session)
YADSN.start()
YADSN.Base.metadata.create_all()


app = Flask(__name__)


@app.route('/')
def hello(subscriptions_manager=YADSNModels.subscriptions_manager):
    subscriber = subscriptions_manager().subscribe(email='rmogilatov@gmail.com')
    print subscriber, subscriber.email, subscriber.id
    return 'Hello, from YADSN Flask Web Application!'


if __name__ == '__main__':
    app.run(port=7000, debug=True)
