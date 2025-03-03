from flask import Flask
from geo_crime_app.config import config

#creating object using a function, helps with creation of multiple instances (better for testing)
def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name, config["default"]))
    return app