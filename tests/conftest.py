from geo_crime_app import create_app
import pytest 

@pytest.fixture()
def app():
    app = create_app('testing')
    return app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()