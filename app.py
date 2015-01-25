"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

from objects.providers import Object

from yadsn import Models, Dependencies
from yadsn import shared
from yadsn.error import BaseError


app = Flask(__name__)
app.config.from_pyfile('local.cfg')


sqlalchemy = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run(port=7000, debug=True)
