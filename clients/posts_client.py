

class PostsClient:
    def __init__(self, api_client):
        self.api = api_client


    def get_posts(self):
        response = self.api.get('/posts')
        response.raise_for_status()
        return response.json()


    def get_post(self, post_id: int):
        response = self.api.get(f'/posts/{post_id}')
        response.raise_for_status()
        return response.json()


    def create_post(self, title: str, body: str, user_id: int):
        payload = {
            'title': title,
            'body': body,
            'user_id': user_id,
        }

        response = self.api.post('/posts', json=payload)
        response.raise_for_status()
        return response.json()


    def update_post(self, post_id: int, title: str, body: str):
        payload= {
            'id': post_id,
            'title': title,
            'body': body,
        }

        response = self.api.put(f'/posts/{post_id}', json=payload)
        response.raise_for_status()
        return response.json()


    def delete_post(self, post_id: int):
        response = self.api.delete(f'/posts/{post_id}')
        response.raise_for_status()
        return response