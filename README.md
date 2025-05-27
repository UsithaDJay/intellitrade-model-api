# 🤖 IntelliTrade Model API

**IntelliTrade Model API** is a lightweight and deployable prediction service designed for the **IntelliTrade** stock trading system. Built with **FastAPI** and powered by a trained **XGBoost** model, this API provides actionable trading signals for each trading day.

### 🧠 What It Does

- Accepts stock market data from the previous **post-market session** to the current **pre-market session**.
- Performs internal feature engineering (e.g., moving averages).
- Feeds engineered features into an XGBoost model.
- Returns a trading action signal — **Buy**, **Sell**, or **Hold** — **before the market opens**.
- Also returns the **model's confidence (probability)** in its prediction.

This allows investors to take informed action at market open and ideally close the position by market close.

---

## 🛠️ Features

- Accepts recent market data from clients (e.g., via frontend or another API).
- Performs in-API feature engineering (e.g., moving averages).
- Serves predictions from a trained XGBoost model.
- Lightweight and production-ready design.
- Easily deployable as a microservice.

---

## 📁 Folder Structure

```bash
intelliTrade-model-api
├── model/
│   ├── load_model.py
│   └── predict.py
├── routes/
│    └── predict.py
├── routes/
│    └── predict.py
├── services/
│   ├── service_compute_features.py
│   └── service_model.py
├── .gitignore
├── main.py                  # FastAPI entry point
├── requirements.txt
├── README.md
└── .env                     # (Optional) environment configuration
```

## ⚙️ Requirements

- Python 3.8+
- pip (for package management)

---

## 🚀 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UsithaDJay/intellitrade-model-api.git
cd intelliTrade-model-api
```

### 2. Create a Virtual Environment

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI Server

```bash
uvicorn main:app --reload
```

Visit your backend at:
- 👉 http://127.0.0.1:8000
- 👉 Swagger UI: http://127.0.0.1:8000/docs

## 📬 How It Works

1. Frontend or another backend service recent market data (e.g., market close prices in last 21 days).
2. The API computes necessary features (e.g., MA_21, rolling statistics).
3. It passes the features into a trained XGBoost model.
4. The model returns a prediction (e.g., Buy).
5. The response is returned as JSON.