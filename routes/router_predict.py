from fastapi import APIRouter, HTTPException

from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_model import ModelService

router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/")
async def predict_endpoint(
    request: PredictRequestSchema,
) -> PredictResponseSchema:
    print(f"Received prediction request for {request.sym_root} on {request.reference_date} for {len(request.daily_raw_data_list)} days of data.")
    if not request.daily_raw_data_list:
        raise HTTPException(status_code=400, detail="No daily raw data provided.")
    # print(f"Request body: {request.model_dump_json(indent=2)}")
    try:
        result = ModelService().predict(input_data=request)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))