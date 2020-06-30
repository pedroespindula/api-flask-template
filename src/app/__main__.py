from flask import Flask
from flask_cors import CORS
from .routes import define_routes

def create_app():
    app = Flask(__name__)

    define_routes(app)

    CORS(app)

    return app
