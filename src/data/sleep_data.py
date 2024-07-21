import pandas as pd

from .generic_loader import load_data_paths
from .helper_funcs import reset_datetime_timeofday


class DataSchema:
    MENTAL_RECOVERY = "mental_recovery"
    PHYSICAL_RECOVERY = "physical_recovery"
    SLEEP_DURATION = "sleep_duration"
    SLEEP_SCORE = "sleep_score"
    WAKE_UP_DATE = "wake_up_date"
    SLEEP_END_TIME = "com.samsung.health.sleep.end_time"


class Labels:
    SLEEP_DATA_LABELS = {
        DataSchema.MENTAL_RECOVERY: "Mental Recovery",
        DataSchema.PHYSICAL_RECOVERY: "Physical Recovery",
        DataSchema.SLEEP_DURATION: "Sleep Duration (h)",
        DataSchema.SLEEP_SCORE: "Sleep Score",
        DataSchema.WAKE_UP_DATE: "Date",
    }


def divide_by_sleep_duration(row, column) -> float:
    if row["sleep_duration"].sum() == 0:
        return None

    return (row[column] * row["sleep_duration"]).sum() / row["sleep_duration"].sum()


def extract_sleep_data(data_paths) -> pd.DataFrame:
    path = data_paths["shealth_sleep"]

    cols = [
        DataSchema.MENTAL_RECOVERY,
        DataSchema.PHYSICAL_RECOVERY,
        DataSchema.SLEEP_DURATION,
        DataSchema.SLEEP_SCORE,
        DataSchema.SLEEP_END_TIME,
    ]

    df = pd.read_csv(
        path,
        dtype={
            DataSchema.MENTAL_RECOVERY: float,
            DataSchema.PHYSICAL_RECOVERY: float,
            DataSchema.SLEEP_DURATION: float,
            DataSchema.SLEEP_SCORE: float,
        },
        parse_dates=[DataSchema.SLEEP_END_TIME],
        usecols=cols,
        sep=",",
        skiprows=1,
        index_col=False,
    )

    # Timezone is off by two hours, data is shifted to compensate
    df[DataSchema.SLEEP_END_TIME] = df[DataSchema.SLEEP_END_TIME] + pd.DateOffset(
        hours=2
    )

    # Set hours, minutes, seconds, and miliseconds to zero
    df[DataSchema.WAKE_UP_DATE] = df[DataSchema.SLEEP_END_TIME].apply(
        reset_datetime_timeofday,
    )

    return df


def prepare_sleep_data(df_sleep) -> pd.DataFrame:
    df_grouped = df_sleep.groupby(DataSchema.WAKE_UP_DATE)

    sleep_duration = (df_grouped[DataSchema.SLEEP_DURATION].sum() / 60).round(2)

    sleep_score = (
        df_grouped.apply(
            divide_by_sleep_duration,
            column=DataSchema.SLEEP_SCORE,
            include_groups=False,
        )
        .rename(DataSchema.SLEEP_SCORE)
        .round(2)
        # / 10
    )

    mental_recovery = (
        df_grouped.apply(
            divide_by_sleep_duration,
            column=DataSchema.MENTAL_RECOVERY,
            include_groups=False,
        )
        .rename(DataSchema.MENTAL_RECOVERY)
        .round(2)
        # / 10
    )

    physical_recovery = (
        df_grouped.apply(
            divide_by_sleep_duration,
            column=DataSchema.PHYSICAL_RECOVERY,
            include_groups=False,
        )
        .rename(DataSchema.PHYSICAL_RECOVERY)
        .round(2)
        # / 10
    )

    df_sleep_scores = pd.concat(
        [sleep_duration, sleep_score, mental_recovery, physical_recovery], axis=1
    )

    df_sleep_scores = df_sleep_scores.dropna()

    return df_sleep_scores


def load_sleep_data() -> pd.DataFrame:
    data = load_data_paths()
    df_sleep = extract_sleep_data(data)
    df_sleep_scores = prepare_sleep_data(df_sleep)
    df_sleep_scores = df_sleep_scores.reset_index()

    return df_sleep_scores
