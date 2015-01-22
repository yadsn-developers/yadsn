"""
YADSN Flask Web Application.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, from YADSN Flask Web Application!'


if __name__ == '__main__':
    app.run(port=7000)
