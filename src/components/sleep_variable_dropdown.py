from dash import dcc, html

from src.data.sleep_data import DataSchema

from . import ids, styles


def render() -> html.Div:
    variables = [
        DataSchema.SLEEP_DURATION,
        DataSchema.MENTAL_RECOVERY,
        DataSchema.PHYSICAL_RECOVERY,
        DataSchema.SLEEP_SCORE,
    ]

    return html.Div(
        children=[
            html.H6("Sleep-Variable"),
            dcc.Dropdown(
                id=ids.SLEEP_VARIABLE_DROPDOWN,
                options=[
                    {"label": variable, "value": variable} for variable in variables
                ],
                value=variables[0],
                multi=True,
                clearable=True,
                persistence="session",
                style=styles.DROPDOWN_STYLE,
            ),
        ]
    )
