import dash
from dash import html

from src.components import styles

dash.register_page(
    __name__,
    title="Cardio-Data",
    name="Cardio-Data",
    description="All things cardio: pulse, fitness, etc.",
    order=2,
)


def layout(**kwargs):
    return html.Div(
        [html.H1("Cardio-Data Analysis"), html.P("Coming soon - Cardio-Data analysis")],
        style=styles.CONTENT_STYLE,
    )
