import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, callback, dcc, html

from src.components import (
    agg_level_dropdown,
    ids,
    layout,
    sleep_duration_line_plot,
    sleep_variable_dropdown,
    styles,
)
from src.data.helper_funcs import aggregate_df, parse_agg_level
from src.data.sleep_data import load_sleep_data

dash.register_page(__name__, title="Sleep-Data", name="Sleep-Data", order=1)

sleep_data = load_sleep_data()


layout = [
    html.Div(
        children=[
            html.H1("Sleep-Data Analysis"),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col([agg_level_dropdown.render()], width=3),
                                dbc.Col([sleep_variable_dropdown.render()], width=3),
                                dbc.Col([layout.draw_kpi_card()], width=3),
                                dbc.Col([layout.draw_kpi_card()], width=3),
                            ],
                            align="center",
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        layout.draw_figure(
                                            id=ids.SLEEP_DURATION_LINE_CHART
                                        )
                                    ],
                                    width=12,
                                )
                            ],
                            align="center",
                        ),
                        html.Br(),
                    ]
                ),
                color="#f8f9fa",
            ),
        ],
        style=styles.CONTENT_STYLE,
    ),
]


@callback(
    Output("store", "data"),
    Input(ids.AGG_LEVEL_DROPDOWN, "value"),
)
def get_data(agg_level):
    agg_freq = parse_agg_level(agg_level)
    sleep_data_agg = aggregate_df(
        sleep_data,
        time_colname="wake_up_date",
        frequency_key=agg_freq,
        agg_operation="mean",
    )
    return sleep_data_agg.to_dict("records")


@callback(
    Output(ids.SLEEP_DURATION_LINE_CHART, "figure"),
    Input("store", "data"),
    Input(ids.SLEEP_VARIABLE_DROPDOWN, "value"),
)
def update(store, sleep_vars):
    df = pd.DataFrame(store)
    return sleep_duration_line_plot.render(df, sleep_vars)
