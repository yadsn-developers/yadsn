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
    catalogs.Services.subscribers()

    @app.route('/')
    def hello(subscribers=catalogs.Services.subscribers):
        try:
            subscriber = subscribers().subscribe(email='test+mail@gmail.com',
                                                 codecha_language='Python',
                                                 http_referrer=request.referrer)
        except BaseError as exception:
            print(exception)
            subscriber = subscribers().get_by_email(email='test+mail@gmail.com')
            subscribers().unsubscribe(subscriber)
            return str(exception)
        else:
            print subscriber, subscriber.email, subscriber.id, subscriber.added_at
            return 'Hello, from YADSN Flask Web Application!'

    return app
