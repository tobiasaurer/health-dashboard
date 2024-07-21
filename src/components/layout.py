import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# from ..pages import cardio_data, home, sleep_data
from . import styles


def create_layout() -> html.Div:
    sidebar = html.Div(
        [
            dcc.Store(id="store", data={}),
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P("Choose the topic you want to analyze", className="lead"),
            dbc.Nav(
                [
                    html.Div(
                        dcc.Link(
                            f"{page['name']}",
                            href=page["relative_path"],
                        )
                    )
                    for page in dash.page_registry.values()
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=styles.SIDEBAR_STYLE,
    )

    content = html.Div(dash.page_container, style=styles.CONTENT_STYLE)
    layout = dbc.Container([sidebar, content], fluid=False)

    return layout


def draw_kpi_card():
    return html.Div(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            [html.H2("Value"), html.H5("Text")],
                            style={"textAlign": "center"},
                        )
                    ]
                )
            ),
        ]
    )


def draw_figure(id):
    return html.Div(
        [
            dbc.Card(
                dbc.CardBody([dcc.Graph(id=id, config={"displayModeBar": False})])
            ),
        ]
    )
