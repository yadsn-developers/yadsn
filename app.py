"""
YADSN Flask Web Application.
"""

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

from yadsn import YADSN, Models, shared
from yadsn.error import BaseError


app = Flask(__name__)
app.config.from_pyfile('local.cfg')


sqlalchemy = SQLAlchemy()
sqlalchemy.init_app(app)


YADSN.start(database_engine=sqlalchemy.engine,
            database_session=sqlalchemy.session,
            config=app.config)
shared.Base.metadata.create_all()


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
