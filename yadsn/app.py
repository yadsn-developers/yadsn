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

    catalogs.Resources.config.update_from(app.config)
    catalogs.Services.users()
    catalogs.Services.subscriptions()

    @app.route('/')
    def hello(subscriptions=catalogs.Services.subscriptions):
        try:
            subscriber = subscriptions().subscribe(email='test+mail@gmail.com',
                                                   codecha_language='Python',
                                                   http_referrer=request.referrer)
        except BaseError as exception:
            print(exception)
            subscriber = subscriptions().get_by_email(email='test+mail@gmail.com')
            subscriptions().unsubscribe(subscriber)
            return str(exception)
        else:
            print subscriber, subscriber.email, subscriber.id, subscriber.added_at
            return 'Hello, from YADSN Flask Web Application!'

    return app
