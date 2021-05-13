from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
message = {"message": "Hello, World"}

@app.route('/')
def index():
    app.logger.debug("url: " + str(request.url))
    print(request.accept_mimetypes.accept_json)
    if request.accept_mimetypes.accept_json:
        return jsonify(message)
    else:
        return "<p>Hello, World</p><br><br><h1>header</h1>"




if __name__ == '__main__':
    app.run()
