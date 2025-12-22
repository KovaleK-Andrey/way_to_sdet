

def test_get_posts(api_client):
    response = api_client.get(f'{api_client.base_url}/posts')
    data = response.json()

    assert response.status_code == 200
    assert len(data) > 0
    assert isinstance(data, list)

    post = data[0]

    assert 'userId' in post
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post


def test_create_post(api_client):
    payload = {
        'title': 'Test title',
        'body': 'Test body',
        'userId': 1
    }

    response = api_client.post(
        f'{api_client.base_url}/posts',
            json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']
    assert 'id' in data


def test_create_post_content_type(api_client):
    response = api_client.post(f'{api_client.base_url}/posts',
                                json={'title': 'Test',
                                   'body': 'Body',
                                   'userId': 1})

    assert response.headers['Content-Type'].startswith('application/json')


def test_create_post_with_empty_body(api_client):
    response = api_client.post(f'{api_client.base_url}/posts',
                             json={})

    assert response.status_code == 201


def test_update_post(api_client):
    payload = {
        'id': 1,
        'title': 'Update title',
        'body': 'Update body',
        'userId': 1
    }

    response = api_client.put(f'{api_client.base_url}/posts/1',
                            json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data['title'] == payload['title']


def test_delete_post(api_client):
    response = api_client.delete(f'{api_client.base_url}/posts/1')

    assert response.status_code == 200