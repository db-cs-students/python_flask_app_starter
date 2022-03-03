from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    """ This prints hello world at the index route
    """
    return "Hello world!"
