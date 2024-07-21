import pandas as pd
from dash import Dash, html

from ..components import agg_level_dropdown, sleep_duration_line_plot, styles


def render(app: Dash, sleep_data: pd.DataFrame):
    content = html.Div(
        children=[
            html.H1("Sleep-Data Analysis"),
            sleep_duration_line_plot.render(app, sleep_data),
            html.Div(
                className="agg-dropdown-container",
                children=[agg_level_dropdown.render(app)],
            ),
        ],
        style=styles.PAGE_STYLE,
    )
    return content
