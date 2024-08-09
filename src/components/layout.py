import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, dcc, html

# from ..pages import cardio_data, home, sleep_data
from . import styles


def create_layout() -> html.Div:
    sidebar = html.Div(
        [
            dbc.Button("Expand Sidebar", id="expand-sidebar", n_clicks=0),
            dbc.Offcanvas(
                [
                    html.P(
                        """
                        Click on the page you want to view to open it.
                        """
                    ),
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
                id="sidebar",
                title="Sidebar",
                is_open=False,
                style=styles.SIDEBAR_STYLE,
            ),
        ]
    )

    content = dbc.Container(
        [dcc.Store(id="store", data={}), dash.page_container],
        style=styles.CONTENT_STYLE,
        fluid=False,
    )
    layout = dbc.Container([sidebar, content], fluid=True)

    return layout


@callback(
    Output("sidebar", "is_open"),
    Input("expand-sidebar", "n_clicks"),
    [State("sidebar", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


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
