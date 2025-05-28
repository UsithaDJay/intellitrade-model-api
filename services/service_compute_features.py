from schemas.schema_predict import PredictRequestSchema
from ml.features import (
    add_prev_day_columns,
    calculate_the_percentage_increment_open_close,
    calculate_precentage_increment_for_price,
    calculate_range_change_metrics,
    calculate_overnight_return,
    compute_ewo_features,
    filter_columns,
    encode_categoricals
)
from utils.utils import to_dataframe
from typing import List

import pandas as pd
# import numpy as np

class ComputeFeaturesService:
    
    def compute_features(input_data: PredictRequestSchema) -> pd.DataFrame:
        df = to_dataframe(input_data.daily_raw_data_list)
        df = df[df["date"] <= pd.to_datetime(input_data.reference_date)].copy()
        df = add_prev_day_columns(df)
        df = calculate_the_percentage_increment_open_close(df)
        df = calculate_precentage_increment_for_price(df)
        df = calculate_range_change_metrics(df)
        df = calculate_overnight_return(df)
        df = compute_ewo_features(df)
        df = encode_categoricals(df, input_data.sym_root)

        # Select only the required input features
        final_df = filter_columns(df)
        # print(final_df.iloc[-1:].to_string())

        return final_df.iloc[-1:]  # return the row for reference_date
    