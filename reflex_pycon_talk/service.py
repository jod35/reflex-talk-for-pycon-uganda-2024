import reflex as rx
from sqlmodel import select, desc
from .models import Post

class PostService:
    def __init__(self):
        self.session = rx.session
    def get_posts(self):
        with self.session() as session:
            statement = select(Post).order_by(desc(Post.created_at))
            return session.exec(statement).all()