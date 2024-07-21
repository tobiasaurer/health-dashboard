import dash
from dash import html

from src.components import styles

dash.register_page(__name__, path="/", title="Home", name="Home", order=0)

IMAGE_PATH = "assets/home_header_image_small.jpg"


def layout(**kwargs):
    # return None
    return html.Div(
        [html.H1("Home"), html.Img(src=IMAGE_PATH)], style=styles.CONTENT_STYLE
    )
