import requests


def test_get_posts_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    assert response.status_code == 200


def test_get_posts_response_body():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    post = data[0]
    assert 'userId' in post
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post


def test_get_single_post():
    post_id = 1
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}')

    assert response.status_code == 200

    post = response.json()
    assert post['id'] == post_id


def test_get_nonexistent_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/999999')

    assert response.status_code == 404