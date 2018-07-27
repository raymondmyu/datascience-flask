from flask import Flask
from flask_bower import Bower

app = Flask(__name__)
Bower(app)

from .core import app_setup
from .api import utils


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
