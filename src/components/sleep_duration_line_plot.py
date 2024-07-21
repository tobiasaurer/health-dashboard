import plotly.graph_objects as go
from dash import html

from ..data.sleep_data import DataSchema, Labels


def render(data, sleep_vars) -> html.Div:
    x_axis = data[DataSchema.WAKE_UP_DATE]
    fig = go.Figure(
        [
            go.Scatter(
                x=x_axis,
                y=data[sleep_var],
                mode="lines",
                name=f"{Labels.SLEEP_DATA_LABELS[sleep_var]}",
            )
            for sleep_var in sleep_vars
        ],
        layout={
            "title": "History of Sleep-Duration",
            "showlegend": True,
            "legend_title": "Legend",
        },
    )
    fig.update_layout(template="plotly")
    fig.update_yaxes(title="Variable Scores")
    fig.update_xaxes(title=Labels.SLEEP_DATA_LABELS[DataSchema.WAKE_UP_DATE])

    return fig
