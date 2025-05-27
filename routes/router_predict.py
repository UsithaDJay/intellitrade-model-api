from http.client import HTTPException
from fastapi import APIRouter

from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_model import ModelService

router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/")
def predict_endpoint(
    request: PredictRequestSchema,
) -> PredictResponseSchema:
    try:
        result = ModelService().predict(raw_data=request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result