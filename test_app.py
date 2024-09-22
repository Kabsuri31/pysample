# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Flask!' in response.data

def test_echo(client):
    """Test the echo endpoint."""
    test_data = {'message': 'Hello, World!'}
    response = client.post('/echo', json=test_data)
    assert response.status_code == 200
    assert response.get_json() == test_data
