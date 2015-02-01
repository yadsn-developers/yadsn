"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from objects.providers import Scoped

from yadsn.catalogs import Resources, Services
from yadsn.error import BaseError


def create_app():
    """
    Application factory.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../local.cfg')

    init_resources(app)
    init_services(app)

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
    Initializes resources.
    """
    Resources.config.update_from(app.config)
    Resources.db().init_app(app)


def init_services(app):
    """
    Initializes services.
    """
    for _, service_provider in Services.__all_providers__(provider_type=Scoped):
        app.before_request(service_provider.in_scope)

        @app.after_request
        def after_request(response_cls):
            service_provider.out_of_scope()
            return response_cls
