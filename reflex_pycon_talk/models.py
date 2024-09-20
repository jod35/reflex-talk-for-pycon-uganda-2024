import reflex as rx
from datetime import datetime

class Post(rx.Model, table=True):
    title : str
    content : str
    created_at : datetime