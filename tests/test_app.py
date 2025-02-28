from geo_crime_app.geo_crime_app import app
import pytest 

@pytest.fixture()
def client():
    client = app.test_client()
    return client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    #assert b"Crime Data" in response.data

"""
def test_crime_route(client):
    #with client.application.app_context():
    response = client.post('/crime', data={'address': 'E10 5NQ', 'crime_date': '2024-01', 'crime_selected': 'drugs'})
    assert response.status_code in [200, 302] 
"""