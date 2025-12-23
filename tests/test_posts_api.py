

def test_get_posts(posts_client):
    posts = posts_client.get_posts()

    assert len(posts) > 0
    assert isinstance(posts, list)

    data = posts[0]
    assert 'userId' in data
    assert 'id' in data
    assert 'title' in data
    assert 'body' in data


def test_create_post(posts_client):
    post = posts_client.create_post(
        title='Test title',
        body='Test body',
        user_id=1,
    )

    assert post['id'] is not None
    assert post['body'] == 'Test body'
    assert post['title'] == 'Test title'


def test_create_post_content_type(api_client):
    response = api_client.post('/posts')

    assert response.headers['Content-Type'].startswith('application/json')


def test_create_post_with_empty_body(api_client):
    response = api_client.post('/posts')

    assert response.status_code == 201


def test_update_post(posts_client):
    posts = posts_client.update_post(
        post_id=1,
        title='Updated',
        body='Updated body')

    assert posts['title'] == 'Updated'
    assert posts['body'] == 'Updated body'



def test_delete_post(posts_client):
    response = posts_client.delete_post(post_id=1)
    assert response.status_code == 200