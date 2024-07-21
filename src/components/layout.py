import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, Input, Output, dcc, html

from ..pages import page_1, page_2, page_home
from . import styles


def create_layout(app: Dash, sleep_data: pd.DataFrame) -> html.Div:
    sidebar = html.Div(
        [
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P("Choose the topic you want to analyze", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Sleep", href="/page-1", active="exact"),
                    dbc.NavLink("Cardio", href="/page-2", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=styles.SIDEBAR_STYLE,
    )

    content = html.Div(id="page-content", style=styles.CONTENT_STYLE)

    layout = html.Div(children=[dcc.Location(id="url"), sidebar, content])

    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return page_home.render(app)
        elif pathname == "/page-1":
            return page_1.render(app, sleep_data)
        elif pathname == "/page-2":
            return page_2.render(app)
        # If the user tries to reach a different page, return a 404 message
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )

    return layout
