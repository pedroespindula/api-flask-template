from tests.fixtures import client

def test_ping_status_code(client):
    response = client.get('/ping/')

    assert response.status_code == 200, 'Should be true'

def test_ping_body(client):
    response = client.get('/ping/')

    assert response.data.decode('utf-8') == 'ping', 'Should be true'
