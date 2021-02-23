import logging
logger = logging.getLogger(__name__)

import pytest
import json

from fastapi.testclient import TestClient
from fastauth.email.server import app

client = TestClient(app)

def test_register_login_server(caplog):
    caplog.set_level(logging.INFO)

    response = client.post('/register', json={
        'email': 'hoge@example.com',
        'password': 'hogehoge',
    })
    assert response.status_code == 200
    logger.info(response.status_code)
    logger.info(response.json())


    response = client.post('/login', json={
        'email': 'hoge@example.com',
        'password': 'hogehoge',
    })
    assert response.status_code == 200
    logger.info(response.status_code)
    logger.info(response.json())

    # Invalid Password
    response = client.post('/login', json={
        'email': 'hoge@example.com',
        'password': 'fugafuga',
    })
    assert response.status_code == 400
    logger.info(response.status_code)
    logger.info(response.json())

    # Duplication
    response = client.post('/register', json={
        'email': 'hoge@example.com',
        'password': '',
    })
    assert response.status_code == 400
    logger.info(response.status_code)
    logger.info(response.json())
