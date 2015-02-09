"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from yadsn import catalogs
from yadsn.error import BaseError


def create_app():
    """
    Application factory.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../local.cfg')

    init_resources(app)
    catalogs.Services.users()
    catalogs.Services.subscriptions()

    @app.route('/')
    def hello(subscriptions_service=catalogs.Services.subscriptions):
        try:
            subscriber = subscriptions_service().subscribe(email='test+mail@gmail.com',
                                                           codecha_language='Python',
                                                           http_referrer=request.referrer)
        except BaseError as exception:
            print(exception)
            subscriptions_service().unsubscribe(email='test+mail@gmail.com')
            return str(exception)
        else:
            print subscriber, subscriber.email, subscriber.id, subscriber.added_at
            return 'Hello, from YADSN Flask Web Application!'

    return app


def init_resources(app):
    """
    Initializes resources.
    """
    catalogs.Resources.config.update_from(app.config)
    catalogs.Resources.db().init_app(app)
