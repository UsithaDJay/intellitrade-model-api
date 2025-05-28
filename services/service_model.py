from ml.load_model import load_model
from ml.predict import predict
from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_compute_features import ComputeFeaturesService
from fastapi import HTTPException

class ModelService:
    def __init__(self):
        self.model = load_model()

    def predict(self, raw_data: PredictRequestSchema) -> PredictResponseSchema:
        features = ComputeFeaturesService.compute_features(raw_data=raw_data)
        # if features.any() is None or features.shape[1] != 90:
        #     raise HTTPException(status_code=400, detail="Invalid features provided.")
        prediction = predict(self.model, features)
        return prediction