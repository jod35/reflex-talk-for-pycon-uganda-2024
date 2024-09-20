from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from .service import PostService
from datetime import datetime

class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime


post_router = APIRouter(
    prefix="/posts"
)

post_service = PostService()

@post_router.get("/", response_model=List[Post])
async def get_post() -> List[Post]:
    posts = post_service.get_posts()

    return posts