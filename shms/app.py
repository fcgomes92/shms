from flask import Flask
from flask_cors import CORS

app = None


def create_app():
    # create the app

    api = Flask(__name__)

    CORS(api)

    api.config.from_object('shms.settings')

    return api


def get_app():
    return create_app()
