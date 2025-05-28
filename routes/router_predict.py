from fastapi import APIRouter, HTTPException

from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_model import ModelService

router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/")
async def predict_endpoint(
    request: PredictRequestSchema,
) -> PredictResponseSchema:
    try:
        result = ModelService().predict(input_data=request)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))