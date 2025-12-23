import pytest
from clients.base_client import BaseClient
from clients.posts_client import PostsClient


@pytest.fixture
def api_client():
    return BaseClient(base_url='https://jsonplaceholder.typicode.com')


@pytest.fixture
def posts_client(api_client):
    return PostsClient(api_client)