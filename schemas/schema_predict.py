from pydantic import BaseModel
from typing import List
from datetime import date

class DailyDataItem(BaseModel):
    date: date
    open: float
    high: float
    low: float
    close: float
    pre_market_price_start: float
    pre_market_price_end: float
    pre_market_price_min: float
    pre_market_price_max: float
    pre_market_price_mean: float
    pre_market_price_std: float
    post_market_price_start: float
    post_market_price_end: float
    post_market_price_min: float
    post_market_price_max: float
    post_market_price_mean: float
    post_market_price_std: float


class PredictRequestSchema(BaseModel):
    sym_root: str
    reference_date: date
    daily_raw_data_list: List[DailyDataItem]


class PredictResponseSchema(BaseModel):
    reference_date: date
    sym_root: str
    prediction: str
    sell_probability: float
    hold_probability: float
    buy_probability: float
