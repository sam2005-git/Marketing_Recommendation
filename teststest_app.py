# tests/test_app.py
import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_recommendations(client):
    response = client.get('/recommendations')
    assert response.status_code == 200
    data = response.get_json()
    assert "recommendations" in data
    assert "Product A" in data["recommendations"]
