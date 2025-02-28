from flask import Flask
from geo_crime_app.config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    return app