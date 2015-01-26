"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from objects.providers import Object

from yadsn.catalogs import (
    Resources,
    Services
)
from yadsn.error import BaseError


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../local.cfg')

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


def init_resources(app):
    """
    Initializes dependencies.
    """
    Resources.db().init_app(app)
    Resources.config.satisfy(Object(app.config))
