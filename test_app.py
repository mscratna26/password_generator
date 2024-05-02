import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data

def test_generate_password(client):
    data = {
        'length': 12,
        'uppercase': True,
        'lowercase': True,
        'numbers': True,
        'symbols': True
    }
    response = client.post('/generate-password', json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'password' in data
    assert len(data['password']) == 12

def test_invalid_password_length(client):
    data = {
        'length': 5,  # Invalid length
        'uppercase': True,
        'lowercase': True,
        'numbers': True,
        'symbols': True
    }
    response = client.post('/generate-password', json=data)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == "Password length should be between 8 and 50 characters."
