from fastapi import FastAPI
from .db import SessionLocal, engine
from .models import Base

app = FastAPI(title="Stock Predictor API")

@app.get("/")
def read_root():
    return {"message": "Stock Predictor API is up and running!"}
