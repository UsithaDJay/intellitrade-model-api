from fastapi import FastAPI, HTTPException
from schemas.schema_predict import PredictRequestSchema, PredictResponseSchema
from services.service_model import ModelService
from routes import router_predict

app = FastAPI()

app.include_router(router_predict.router)

@app.get("/")
def root():
    return {"message": "Model API is running!"}

# @app.post("/predict", response_model=PredictResponseSchema)
# def predict_endpoint(request: PredictRequestSchema):
#     try:
#         result = ModelService().predict(raw_data=request)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     return result
