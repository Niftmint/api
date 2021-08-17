# author: Rui Maximo

# create an empty file called conftest.py in the root directory
# for pytest to be able to resolve this module
from app import app

import pytest
import json

url = '/'

@pytest.fixture
def client():
    flask_app = app()
    client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello World!'

