import reflex as rx
from rxconfig import config

from .data import posts
from .pages import post_detail, index
from .models import Post
from .routes import post_router
from fastapi.responses import JSONResponse
from fastapi import status
from .state import PostState


def index_route():
    return {"message": "I am an API endpoint"}


app = rx.App()

# some frontend stuff
app.add_page(index, on_load=[PostState.load_posts])
app.add_page(post_detail)

# this is some backend stuff
app.api.add_api_route(path="/", endpoint=index_route)
app.api.include_router(post_router)


@app.api.exception_handler(500)
async def internal_server_error(request, exception):
    return JSONResponse(
        content={"message": "Internal Server Error", "error": str(exception)},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
