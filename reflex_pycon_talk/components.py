import reflex as rx
from . import styles
from .state import PostState


def post(title: str, content: str) -> rx.Component:

    return rx.card(
        rx.box(
            rx.heading(
                rx.link(
                    title,
                    href=f"/{PostState.current_post_slug}",
                    style=styles.post_heading,
                ),
                size="4",
                on_click=PostState.set_current_post(
                    {"title": title, "content": content}
                ),
            ),
        ),
        rx.box(rx.text(content)),
        style=styles.post_container,
    )
