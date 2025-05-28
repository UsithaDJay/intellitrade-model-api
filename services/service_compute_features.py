from schemas.schema_predict import PredictRequestSchema

import pandas as pd
import numpy as np

class ComputeFeaturesService:
    def compute_features(raw_data: PredictRequestSchema) -> pd.DataFrame:
        # TODO: Implement the feature computation logic
        # feature list
        features = raw_data.raw_data
        # df = pd.DataFrame([features], columns=["MA_21", "feature2", "feature3"])
        # features = [
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        #     0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, None
        # ]

        # Convert to NumPy array and reshape
        input_feature_array = np.array(features).reshape(1, -1)     # shape: (1, 90)

        # Ensure the DataFrame has the correct shape and columns
        # if df.shape[1] != 3:
        #     raise ValueError("Invalid number of features provided.")
        
        # Add any additional feature engineering steps here
        return input_feature_array