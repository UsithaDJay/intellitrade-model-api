from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class DailyDataItem(BaseModel):
    date: date
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    pre_market_price_start: float
    pre_market_price_end: float
    pre_market_price_min: float
    pre_market_price_max: float
    pre_market_price_mean: float
    pre_market_price_std: float
    post_market_price_start: Optional[float] = None
    post_market_price_end: Optional[float] = None
    post_market_price_min: Optional[float] = None
    post_market_price_max: Optional[float] = None
    post_market_price_mean: Optional[float] = None
    post_market_price_std: Optional[float] = None


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
