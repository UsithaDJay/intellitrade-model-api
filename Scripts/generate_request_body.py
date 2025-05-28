import json
import random
from datetime import datetime, timedelta
# Configuration
sym_root = "AAPL"
reference_date = datetime.strptime("2024-05-21", "%Y-%m-%d")

# Generate 40 days of data ending at reference_date
num_days = 40

daily_raw_data_list = []
base_price = 170.0

current_date = reference_date + timedelta(days=1)
# Generate daily data for the last num_days days
while len(daily_raw_data_list) < num_days:

    current_date = current_date - timedelta(days=1)
    # Skip weekends
    if current_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        continue


    # Simulate day price
    open_price = round(base_price + random.uniform(-1, 1), 2)
    high_price = round(open_price + random.uniform(0.5, 2.0), 2)
    low_price = round(open_price - random.uniform(0.5, 2.0), 2)
    close_price = round(random.uniform(low_price, high_price), 2)

    # Pre-market simulation
    pre_start = round(open_price + random.uniform(-1, 1), 2)
    pre_end = round(pre_start + random.uniform(-0.5, 0.5), 2)
    pre_min = round(min(pre_start, pre_end) - random.uniform(0, 0.5), 2)
    pre_max = round(max(pre_start, pre_end) + random.uniform(0, 0.5), 2)
    pre_mean = round((pre_start + pre_end) / 2, 2)
    pre_std = round(random.uniform(0.2, 0.6), 2)

    # Post-market simulation
    post_start = round(close_price + random.uniform(-0.5, 0.5), 2)
    post_end = round(post_start + random.uniform(-0.3, 0.3), 2)
    post_min = round(min(post_start, post_end) - random.uniform(0, 0.5), 2)
    post_max = round(max(post_start, post_end) + random.uniform(0, 0.5), 2)
    post_mean = round((post_start + post_end) / 2, 2)
    post_std = round(random.uniform(0.2, 0.5), 2)

    day_data = {
        "date": current_date.strftime("%Y-%m-%d"),
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "pre_market_price_start": pre_start,
        "pre_market_price_end": pre_end,
        "pre_market_price_min": pre_min,
        "pre_market_price_max": pre_max,
        "pre_market_price_mean": pre_mean,
        "pre_market_price_std": pre_std,
        "post_market_price_start": post_start,
        "post_market_price_end": post_end,
        "post_market_price_min": post_min,
        "post_market_price_max": post_max,
        "post_market_price_mean": post_mean,
        "post_market_price_std": post_std
    }

    daily_raw_data_list.append(day_data)


# Final request body
request_body = {
    "sym_root": sym_root,
    "reference_date": reference_date.strftime("%Y-%m-%d"),
    "daily_raw_data_list": daily_raw_data_list
}

# Print request
print("Sample Request Body:\n")
print(json.dumps(request_body, indent=2))
