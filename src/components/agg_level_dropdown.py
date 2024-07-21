from dash import dcc, html

from . import ids, styles


def render() -> html.Div:
    agg_levels = ["Day", "Week", "Month", "Quarter", "Year"]

    return html.Div(
        children=[
            html.H6("Aggregation-level"),
            dcc.Dropdown(
                id=ids.AGG_LEVEL_DROPDOWN,
                options=[
                    {"label": agg_level, "value": agg_level} for agg_level in agg_levels
                ],
                value=agg_levels[0],
                multi=False,
                clearable=False,
                persistence="session",
                style=styles.DROPDOWN_STYLE,
            ),
        ]
    )
