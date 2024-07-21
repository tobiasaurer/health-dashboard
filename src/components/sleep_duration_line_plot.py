import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.helper_funcs import aggregate_df, parse_agg_level
from ..data.sleep_data import DataSchema
from . import ids


def render(app: Dash, sleep_data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.SLEEP_DURATION_LINE_CHART, "children"),
        Input(ids.AGG_LEVEL_DROPDOWN, "value"),
    )
    def update_line_plot(agg_level: str) -> html.Div:
        agg_level_parsed = parse_agg_level(agg_level)
        sleep_data_aggregated = aggregate_df(
            sleep_data, DataSchema.WAKE_UP_DATE, agg_level_parsed, "mean"
        )

        fig = px.line(
            data_frame=sleep_data_aggregated.reset_index(),
            x=DataSchema.WAKE_UP_DATE,
            y=[DataSchema.SLEEP_DURATION, DataSchema.MENTAL_RECOVERY],
            labels={
                DataSchema.SLEEP_DURATION: "Sleep Duration (h)",
                DataSchema.WAKE_UP_DATE: "Date",
            },
            title="History of Sleep-Duration",
            template="plotly",
            range_y=[0, (sleep_data_aggregated[DataSchema.SLEEP_DURATION].max() + 0.5)],
        )
        fig.update_yaxes(title="Sleep-Duration")

        return html.P("IS THIS TEXT SHOWN????", className="lead")
        # return html.Div(dcc.Graph(figure=fig), id=ids.SLEEP_DURATION_LINE_CHART)

    # return html.Div(id=ids.SLEEP_DURATION_LINE_CHART)
    return html.P("IS THIS TEXT SHOWN OR WHAT????", className="lead")
