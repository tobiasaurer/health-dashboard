import pandas as pd


def reset_datetime_timeofday(row):
    return row.replace(hour=0, minute=0, second=0, microsecond=0)


def aggregate_df(
    df: pd.DataFrame, time_colname: str, frequency_key: str, agg_operation: str
) -> pd.DataFrame:
    if agg_operation == "mean":
        return df.resample(frequency_key, on=time_colname).mean()

    elif agg_operation == "sum":
        return df.resample(frequency_key, on=time_colname).sum()

    else:
        return df


def parse_agg_level(agg_level_in: str) -> str:
    PARSING_DICT = {
        "Day": "D",
        "Week": "W",
        "Month": "MS",
        "Quarter": "QS",
        "Year": "YS",
    }

    return PARSING_DICT[agg_level_in]
