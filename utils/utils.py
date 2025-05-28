from schemas.schema_predict import DailyDataItem

from typing import List
import pandas as pd


def to_dataframe(daily_raw_data_list: List[DailyDataItem]) -> pd.DataFrame:
    df = pd.DataFrame([item.dict() for item in daily_raw_data_list])
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(by="date").reset_index(drop=True)
    return df