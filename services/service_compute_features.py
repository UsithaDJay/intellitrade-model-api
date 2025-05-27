from schemas.schema_predict import PredictRequestSchema

import pandas as pd

class ComputeFeaturesService:
    def compute_features(self, raw_data: PredictRequestSchema) -> pd.DataFrame:
        # TODO: Implement the feature computation logic
        features = raw_data.raw_data
        df = pd.DataFrame([features], columns=["MA_21", "feature2", "feature3"])

        # Ensure the DataFrame has the correct shape and columns
        if df.shape[1] != 3:
            raise ValueError("Invalid number of features provided.")
        
        # Add any additional feature engineering steps here
        return df