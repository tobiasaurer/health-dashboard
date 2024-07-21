from dash import Dash, html

from ..components import styles

IMAGE_PATH = "assets/home_header_image_small.jpg"


def render(app: Dash):
    content = html.Div(
        [html.H1("Home-Page"), html.Img(src=IMAGE_PATH)], style=styles.PAGE_STYLE
    )

    return content
