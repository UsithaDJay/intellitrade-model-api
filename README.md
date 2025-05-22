# 📊 IntelliTrade-backend

This backend system is designed to simulate a real-time stock prediction platform using historical OHLCV and extended hours data. It is implemented using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, and supports model training, prediction, and data labeling workflows.

---

## 🛠️ Features

- Store OHLCV and extended hours data per symbol and date.
- Store processed features and labels for prediction tasks.
- Simulate real-time daily data updates.
- Predict buy/sell/hold decisions via a trained ML model.
- Allow model retraining at configurable frequencies.
- Built with modular and maintainable structure.

---

## 📁 Folder Structure

```bash
IntelliTrade-backend
├── app/
│ ├── main.py # FastAPI entry point
│ ├── db.py # DB engine and session setup
│ ├── models.py # SQLAlchemy models
│ ├── crud.py # CRUD operations
│ ├── schemas.py # Pydantic schemas
│ ├── utils/
│ │ ├── preprocessing.py # Preprocessing functions
│ │ └── model.py # ML model training/prediction
│
├── requirements.txt
├── README.md
└── .env # Environment variables
```

## ⚙️ Requirements

- Python 3.8+
- PostgreSQL
- pip

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UsithaDJay/IntelliTrade-backend.git
cd IntelliTrade-backend
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

### 4. Create and Configure PostgreSQL Database(Skip this step for now)

- Make sure PostgreSQL is installed and running.

#### Create a new database named stock_db:
```bash
psql -U postgres
CREATE DATABASE stock_db;
```

#### Create a .env file at the root level:
```bash
DATABASE_URL=postgresql://postgres:yourpassword@localhost/stock_db
```

Update DATABASE_URL in models.py or db.py to use environment variable (optional but recommended).

#### Initialize Database
```bash
python create_tables.py
```

This will create the required tables: ohlcv_data, extended_hours_data, and processed_data.

### 5. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Visit your backend at:
- 👉 http://127.0.0.1:8000
- 👉 Swagger UI: http://127.0.0.1:8000/docs

## ✅ Example Workflow

1. Collect and store daily OHLCV and extended hours data.
2. Run preprocessing to create feature vectors.
3. Store processed data and labels in the database.
4. Train the model using historical data.
5. Simulate new daily data and get predictions.
6. Update labels when the next day’s data becomes available.
7. Retrain model periodically based on your settings (daily/weekly/monthly).