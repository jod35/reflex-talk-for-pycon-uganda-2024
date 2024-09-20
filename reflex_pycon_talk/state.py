import reflex as rx
from typing import List
from httpx import Client

class PostState(rx.State):
    post : dict = {}
    posts: List[dict] = []


    def set_current_post(self, post: dict):
        self.post = post

    @rx.var
    def current_post_slug(self):
        return self.post.get('title', '').lower().replace(' ', '-')
    

    def load_posts(self):
        client = Client()

        with client.get('http://localhost:8000/posts',timeout=None) as response:
            print(response.json())
            self.posts = response.json()

