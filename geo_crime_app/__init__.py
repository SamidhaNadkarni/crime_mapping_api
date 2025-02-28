from flask import Flask
from geo_crime_app.config import config

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name, config["default"]))
    return app

app_config = config