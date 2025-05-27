from model.load_model import load_model
from model.predict import predict
from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_compute_features import ComputeFeaturesService
from fastapi import HTTPException

class ModelService:
    def __init__(self):
        self.model = load_model()

    def predict(self, raw_data: PredictRequestSchema) -> PredictResponseSchema:
        features = ComputeFeaturesService.compute_features(raw_data)
        if not features:
            raise HTTPException(status_code=400, detail="Invalid features provided.")
        prediction = predict(self.model, features)
        return prediction