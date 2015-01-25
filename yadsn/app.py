"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

from objects.providers import Object

from yadsn import Models, Dependencies
from yadsn import shared
from yadsn.error import BaseError


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../local.cfg')

    sqlalchemy = SQLAlchemy()
    sqlalchemy.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, sqlalchemy)

    with app.app_context():
        Dependencies.database_session.satisfy(Object(sqlalchemy.session))
        Dependencies.config.satisfy(Object(app.config))

        shared.Base.metadata.bind = sqlalchemy.engine
        sqlalchemy.Model.metadata = shared.Base.metadata

    @app.route('/')
    def hello(subscriptions_manager=Models.subscriptions_manager):
        try:
            subscriber = subscriptions_manager().subscribe(email='test+mail@gmail.com',
                                                           codecha_language='Python',
                                                           http_referrer=request.referrer)
        except BaseError as exception:
            return exception.args[0]
        else:
            print subscriber, subscriber.email, subscriber.id
            return 'Hello, from YADSN Flask Web Application!'

    return app
