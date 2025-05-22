from sqlalchemy import Column, Integer, Float, String, Date
from .db import Base

class OHLCVData(Base):
    __tablename__ = "ohlcv_data"

    id = Column(Integer, primary_key=True, index=True)
    sym_root = Column(String, index=True)
    date = Column(Date, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)


class ExtendedHourData(Base):
    __tablename__ = "extended_hour_data"

    id = Column(Integer, primary_key=True, index=True)
    sym_root = Column(String, index=True)
    date = Column(Date, index=True)
    pre_market_volume = Column(Float)
    post_market_volume = Column(Float)
    pre_market_price_mean = Column(Float)
    post_market_price_mean = Column(Float)
    pre_market_price_std = Column(Float)
    post_market_price_std = Column(Float)
    pre_market_price_min = Column(Float)
    post_market_price_min = Column(Float)
    pre_market_price_max = Column(Float)
    post_market_price_max = Column(Float)
