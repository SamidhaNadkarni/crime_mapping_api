
def test_config(app):
    assert app.config['TESTING']

def test_response(client):
    response = client.get('/')
    assert response.status_code == 200