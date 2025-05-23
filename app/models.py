from sqlalchemy import Column, Integer, String, Float, Date, BigInteger, JSON, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .db import Base

# --- USER MANAGEMENT ---
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)

    trades = relationship("UserTrade", back_populates="user")


# --- TICKER / SYMBOL METADATA ---
class Ticker(Base):
    __tablename__ = 'tickers'

    id = Column(Integer, primary_key=True, index=True)
    sym_root = Column(String, unique=True, index=True, nullable=False)
    company_name = Column(String)

    daily_data = relationship("DailyMarketData", back_populates="ticker")
    processed_data = relationship("ProcessedData", back_populates="ticker")
    trades = relationship("UserTrade", back_populates="ticker")
    model_outputs = relationship("ModelOutput", back_populates="ticker")


# --- DAILY MARKET DATA (COMBINED) ---
class DailyMarketData(Base):
    __tablename__ = 'daily_market_data'

    id = Column(Integer, primary_key=True, index=True)
    ticker_id = Column(Integer, ForeignKey('tickers.id'))
    date = Column(Date, index=True)
    day_of_week = Column(String)  # 'Monday', 'Tuesday', etc.
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(BigInteger)
    pre_market_volume = Column(BigInteger)
    pre_market_price_mean = Column(Float)
    pre_market_price_std = Column(Float)
    pre_market_price_min = Column(Float)
    pre_market_price_max = Column(Float)
    pre_market_price_median = Column(Float)
    pre_market_price_start = Column(Float)
    pre_market_price_end = Column(Float)
    post_market_volume = Column(BigInteger)
    post_market_price_mean = Column(Float)
    post_market_price_std = Column(Float)
    post_market_price_min = Column(Float)
    post_market_price_max = Column(Float)
    post_market_price_median = Column(Float)
    post_market_price_start = Column(Float)
    post_market_price_end = Column(Float)

    ticker = relationship("Ticker", back_populates="daily_data")


# --- PROCESSED FEATURES & LABELS ---
class ProcessedData(Base):
    __tablename__ = 'processed_data'

    id = Column(Integer, primary_key=True, index=True)
    ticker_id = Column(Integer, ForeignKey('tickers.id'))
    date = Column(Date, index=True)
    feature_vector = Column(JSON)
    label = Column(Integer)

    ticker = relationship("Ticker", back_populates="processed_data")


# --- MODEL OUTPUT ---
class ModelOutput(Base):
    __tablename__ = 'model_outputs'

    id = Column(Integer, primary_key=True, index=True)
    ticker_id = Column(Integer, ForeignKey('tickers.id'))
    date = Column(Date, index=True)
    predicted_action = Column(String)  # 'buy', 'sell', 'hold'
    confidence_score = Column(Float)

    ticker = relationship("Ticker", back_populates="model_outputs")


# --- USER TRADE DECISIONS ---
class UserTrade(Base):
    __tablename__ = 'user_trades'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ticker_id = Column(Integer, ForeignKey('tickers.id'))
    entry_date = Column(Date, index=True)
    exit_date = Column(Date, index=True)
    action = Column(String)  # 'buy', 'sell'
    quantity = Column(Integer)
    entry_price = Column(Float)
    exit_price = Column(Float)
    profit_or_loss = Column(Float)

    user = relationship("User", back_populates="trades")
    ticker = relationship("Ticker", back_populates="trades")
