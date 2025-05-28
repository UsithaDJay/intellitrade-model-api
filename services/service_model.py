from ml.load_model import load_model
from ml.predict import predict
from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_compute_features import ComputeFeaturesService
from fastapi import HTTPException

class ModelService:
    def __init__(self):
        self.model = load_model()

    def predict(self, input_data: PredictRequestSchema) -> PredictResponseSchema:
        features = ComputeFeaturesService.compute_features(input_data=input_data)
        # if features.any() is None or features.shape[1] != 90:
        #     raise HTTPException(status_code=400, detail="Invalid features provided.")
        prediction, sell_probability, hold_probability, buy_probability = predict(self.model, features)
        reference_date = input_data.reference_date.strftime("%Y-%m-%d")
        sym_root = input_data.sym_root
        response = PredictResponseSchema(
            reference_date=reference_date,
            sym_root=sym_root,
            prediction=prediction,
            sell_probability=sell_probability,
            hold_probability=hold_probability,
            buy_probability=buy_probability
        )
        return response