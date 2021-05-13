import os

from flask import Flask, request, jsonify
import logging


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    message = {"message": "Hello, World"}

    @app.route('/', methods=("GET", "POST"))
    def index():
        app.logger.debug("url: " + str(request.url))
        if request.accept_mimetypes.accept_json:
            return jsonify(message)
        else:
            return "<p>Hello, World</p>"

    return app
