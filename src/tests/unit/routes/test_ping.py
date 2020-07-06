# pylint: disable=W0611,W0621

from tests.fixtures import client

def test_ping_status_code(client):
    response = client.get('/ping/')

    assert response.status_code == 200, 'Should be 200'

def test_ping_body(client):
    response = client.get('/ping/')

    assert response.data.decode('utf-8') == 'ping', 'Should return "ping"'

def test_ping_cannot_post(client):
    response = client.post('/ping/')

    assert response.status_code == 405, 'Should not allow POST method'

def test_ping_cannot_put(client):
    response = client.put('/ping/')

    assert response.status_code == 405, 'Should not allow PUT method'

def test_ping_cannot_patch(client):
    response = client.patch('/ping/')

    assert response.status_code == 405, 'Should not allow PATCH method'

def test_ping_cannot_delete(client):
    response = client.delete('/ping/')

    assert response.status_code == 405, 'Should not allow DELETE method'
