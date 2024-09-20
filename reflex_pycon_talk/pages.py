import reflex as rx
from .state import PostState
from .components import post
from .data import posts
from .state import PostState

@rx.page(route="/[post_id]",title="Detail")
def post_detail() -> rx.Component:
    # Post Detail Page

    return rx.container(
        rx.heading("Post Detail"),
        rx.box(rx.text("This is the post detail page."))
    )


def render_post(post_:dict):
    return post(post_["title"], post_["content"])

def index() -> rx.Component:
    return rx.container(
        rx.heading("Hello World"),
        rx.box(
            rx.foreach(
                PostState.posts,
                render_post
            ),
            class_name="posts"
        )
    )