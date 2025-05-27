from pydantic import BaseModel
from typing import List

class PredictRequestSchema(BaseModel):
    raw_data: List[float]  # Feature vector e.g. [MA_21, feature2, feature3, ...]

class PredictResponseSchema(BaseModel):
    prediction: str
    sell_probability: float
    hold_probability: float
    buy_probability: float
