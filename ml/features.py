from constants.constants import INPUT_FEATURE_COLUMNS, ALL_SYM_ROOT_DUMMIES, ALL_DAY_OF_WEEK_DUMMIES
import pandas as pd

def add_prev_day_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("date") # Ensure chronological order
    df['PREV_OPEN'] = df['open'].shift(1)
    df['PREV_CLOSE'] = df['close'].shift(1)
    df['PREV_HIGH'] = df['high'].shift(1)
    df['PREV_LOW'] = df['low'].shift(1)
    df['PREV_post_market_price_mean'] = df['post_market_price_mean'].shift(1)
    df['PREV_post_market_price_std'] = df['post_market_price_std'].shift(1)
    return df

def compute_ewo_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("date")
    df["MA_5"] = df["close"].rolling(window=5).mean().shift(1)
    df["MA_35"] = df["close"].rolling(window=35).mean().shift(1)
    df["EWO"] = (df["MA_5"] - df["MA_35"]) / (df["MA_5"] + df["MA_35"])
    df["EWO_lag_1"] = df["EWO"].shift(1)
    df["EWO_lag_2"] = df["EWO"].shift(2)
    return df

def calculate_range_change_metrics(df: pd.DataFrame) -> pd.DataFrame:
    # Sort by SYM_ROOT and DATE to preserve time order for percent change calculation
    df = df.sort_values(by=['date'])

    # Range-based change as a percentage of the minimum value
    df['pre_market_range_change'] = ((df['pre_market_price_max'] - df['pre_market_price_min'])
                                     / df['pre_market_price_min']) * 100
    df['prev_post_market_range_change'] = ((df['post_market_price_max'].shift(1) - df['post_market_price_min'].shift(1))
                                      / df['post_market_price_min'].shift(1)) * 100

    # Spread relative to the mean as a percentage (to measure volatility)
    df['pre_market_spread'] = ((df['pre_market_price_max'] - df['pre_market_price_min']) / df['pre_market_price_mean'])*100
    df['prev_post_market_spread'] = ((df['post_market_price_max'].shift(1) - df['post_market_price_min'].shift(1)) / df['post_market_price_mean'].shift(1))*100

    return df

def calculate_overnight_return(df: pd.DataFrame) -> pd.DataFrame:
  df = df.sort_values(by=['date'])

  # Calculate the full overnight return from prev day post market start to day's pre market end
  df['overnight_mean'] = (df['pre_market_price_mean'] + df['post_market_price_mean'].shift(1))/2
  df['full_overnight_return'] = ((df['pre_market_price_end'] - df['post_market_price_start'].shift(1))/df['overnight_mean'])*100

  df['pre_market_return'] = ((df['pre_market_price_end'] - df['pre_market_price_start'])/df['pre_market_price_start'])*100
  df['post_market_return'] = ((df['post_market_price_end'].shift(1) - df['post_market_price_start'].shift(1))/df['post_market_price_start'].shift(1))*100

  return df

# Function to calculate percentage increment
def calculate_percentage_increment(df: pd.DataFrame, col, window) -> pd.DataFrame:
    df = df.sort_values(by="date")
    df[f"{col}_avg_{window}"] = df[col].rolling(window=window, min_periods=window).mean().shift(1)

    df[f"{col}_avg_{window}_increment"] = ((df[col] - df[f"{col}_avg_{window}"]) / df[f"{col}_avg_{window}"]) * 100

    return df

def calculate_precentage_increment_for_price(df: pd.DataFrame) -> pd.DataFrame:
  df = calculate_percentage_increment(df, 'pre_market_price_mean',1)
  df = calculate_percentage_increment(df, 'pre_market_price_mean',3)
  df = calculate_percentage_increment(df, 'pre_market_price_mean',5)
  df = calculate_percentage_increment(df, 'pre_market_price_mean',10)
  df = calculate_percentage_increment(df, 'pre_market_price_mean',22)

  df = calculate_percentage_increment(df, 'pre_market_price_std',3)
  df = calculate_percentage_increment(df, 'pre_market_price_std',5)
  df = calculate_percentage_increment(df, 'pre_market_price_std',10)

  df = calculate_percentage_increment(df, 'PREV_post_market_price_mean',1)
  df = calculate_percentage_increment(df, 'PREV_post_market_price_mean',3)
  df = calculate_percentage_increment(df, 'PREV_post_market_price_mean',5)
  df = calculate_percentage_increment(df, 'PREV_post_market_price_mean',10)
  df = calculate_percentage_increment(df, 'PREV_post_market_price_mean',22)

  df = calculate_percentage_increment(df, 'PREV_post_market_price_std',3)
  df = calculate_percentage_increment(df, 'PREV_post_market_price_std',5)
  df = calculate_percentage_increment(df, 'PREV_post_market_price_std',10)

  return df

def calculate_the_percentage_increment_open_close(df: pd.DataFrame) -> pd.DataFrame:
  df = calculate_percentage_increment(df, 'PREV_OPEN',1)
  df = calculate_percentage_increment(df, 'PREV_OPEN',3)
  df = calculate_percentage_increment(df, 'PREV_OPEN',5)
  df = calculate_percentage_increment(df, 'PREV_OPEN',9)
  df = calculate_percentage_increment(df, 'PREV_OPEN',12)

  df = calculate_percentage_increment(df, 'PREV_CLOSE',1)
  df = calculate_percentage_increment(df, 'PREV_CLOSE',3)
  df = calculate_percentage_increment(df, 'PREV_CLOSE',5)
  df = calculate_percentage_increment(df, 'PREV_CLOSE',9)
  df = calculate_percentage_increment(df, 'PREV_CLOSE',12)

  df = calculate_percentage_increment(df, 'PREV_HIGH',1)
  df = calculate_percentage_increment(df, 'PREV_HIGH',3)
  df = calculate_percentage_increment(df, 'PREV_HIGH',5)
  df = calculate_percentage_increment(df, 'PREV_HIGH',9)
  df = calculate_percentage_increment(df, 'PREV_HIGH',12)

  df = calculate_percentage_increment(df, 'PREV_LOW',1)
  df = calculate_percentage_increment(df, 'PREV_LOW',3)
  df = calculate_percentage_increment(df, 'PREV_LOW',5)
  df = calculate_percentage_increment(df, 'PREV_LOW',9)
  df = calculate_percentage_increment(df, 'PREV_LOW',12)

  return df

def encode_categoricals(df: pd.DataFrame, sym_root) -> pd.DataFrame:
    df = df.copy()
    df['SYM_ROOT'] = sym_root
    df['DAY_OF_WEEK'] = df['date'].dt.day_name()  # e.g., 'Monday', 'Tuesday', ...

    df = pd.get_dummies(df, columns=['SYM_ROOT', 'DAY_OF_WEEK'], drop_first=False)

    for col in ALL_SYM_ROOT_DUMMIES + ALL_DAY_OF_WEEK_DUMMIES:
        if col not in df.columns:
            df[col] = 0
    return df

def filter_columns(df: pd.DataFrame) -> pd.DataFrame:
   df = df.loc[:, INPUT_FEATURE_COLUMNS]

   return df