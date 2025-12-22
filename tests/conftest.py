import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json'
    })
    session.base_url = BASE_URL
    return session