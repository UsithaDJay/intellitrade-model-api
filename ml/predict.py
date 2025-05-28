from constants.constants import PROBABILITY_THRESHOLD
import pandas as pd
import logging

def predict(model, input_features: pd.DataFrame):
    logger = logging.getLogger(__name__)
    logger.info("Features shape: %s", input_features.shape)
    logger.info("Feature columns: %s", input_features.columns.tolist())
    logger.info("First row: %s", input_features.iloc[0].to_dict() if not input_features.empty else "Empty")
    model_prediction_id = model.predict(input_features)
    pred_probabilities = model.predict_proba(input_features)
    if len(model_prediction_id) == 0 or len(pred_probabilities) == 0:
        raise ValueError("Model prediction returned empty results.")
    if len(model_prediction_id) != 1:
        raise ValueError("Prediction should return exactly one value.")
    if len(pred_probabilities[0]) != 3:
        raise ValueError("Prediction probabilities should return exactly three values for buy, hold, and sell.")
    
    # Apply custom threshold logic
    threshold = PROBABILITY_THRESHOLD
    sell_probability = pred_probabilities[0][0]
    hold_probability = pred_probabilities[0][1]
    buy_probability = pred_probabilities[0][2]
    if buy_probability > threshold:
        prediction = "Buy"
    elif sell_probability > threshold:
        prediction = "Sell"
    else:
        prediction = "Hold"

    
    
    # if (prediction_id[0] == 1):
    #     prediction = "Hold"
    # elif (prediction_id[0] == 2):
    #     prediction = "Buy"
    # elif (prediction_id[0] == 0):
    #     prediction = "Sell"
    # else:
    #     raise ValueError("Prediction ID is not valid. Expected 0, 1, or 2.")
    
    
    print(f"Prediction: {prediction}, Sell Probability: {sell_probability}, Hold Probability: {hold_probability}, Buy Probability: {buy_probability}")

    return prediction, sell_probability, hold_probability, buy_probability
