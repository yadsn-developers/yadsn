"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from objects.providers import Object

from yadsn.catalogs.services import Services
from yadsn.catalogs.resources import Resources
from yadsn.extensions import db, migrate
from yadsn.error import BaseError


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../local.cfg')

    init_extensions(app)
    init_resources(app)

    @app.route('/')
    def hello(subscriptions=Services.subscriptions):
        try:
            subscriber = subscriptions().subscribe(email='test+mail@gmail.com',
                                                   codecha_language='Python',
                                                   http_referrer=request.referrer)
        except BaseError as exception:
            return exception.args[0]
        else:
            print subscriber, subscriber.email, subscriber.id
            return 'Hello, from YADSN Flask Web Application!'

    return app


def init_extensions(app):
    """
    Initializes Flask extensions.
    """
    db.init_app(app)
    migrate.init_app(app, db)


def init_resources(app):
    """
    Initializes YADS dependencies.
    """
    with app.app_context():
        # Config binding.
        Resources.config.satisfy(Object(app.config))
        Resources.db.satisfy(Object(db))
