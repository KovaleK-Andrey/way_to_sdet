import requests


BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_create_post():
    payload = {
        'title': 'Test title',
        'body': 'Test body',
        'userId': 1
    }

    response = requests.post(
        f'{BASE_URL}/posts',
            json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']
    assert 'id' in data


def test_create_post_content_type():
    response = requests.post(f'{BASE_URL}/posts',
                                json={'title': 'Test',
                                   'body': 'Body',
                                   'userId': 1})

    assert response.headers['Content-Type'].startswith('application/json')


def test_create_post_with_empty_body():
    response = requests.post(f'{BASE_URL}/posts',
                             json={})

    assert response.status_code == 201


def test_update_post():
    payload = {
        'id': 1,
        'title': 'Update title',
        'body': 'Update body',
        'userId': 1
    }

    response = requests.put(f'{BASE_URL}/posts/1',
                            json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data['title'] == payload['title']


def test_delete_post():
    response = requests.delete(f'{BASE_URL}/posts/1')

    assert response.status_code == 200