import pickle

def load_model(model_path="ml/model/xgb_model.pkl"):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model
