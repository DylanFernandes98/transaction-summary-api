# Transaction Summary API
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
[![codecov](https://codecov.io/gh/DylanFernandes98/transaction-summary-api/branch/main/graph/badge.svg)](https://codecov.io/gh/DylanFernandes98/transaction-summary-api)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)


This project implements a RESTful API built with FastAPI that processes uploaded CSV data and returns per-user transaction summaries.

The goal is to demonstrate clean, maintainable, and testable backend design - including file uploads, data validation, and analytical summaries using Pandas.

## 🚀 Features

- **/upload** → Accepts CSV file uploads and validates file format.  
- **/summary/{user_id}** → Returns the minimum, maximum, and mean transaction amount for a given user.  
- **Error handling:**  
  - 400 → Non-CSV upload or missing data  
  - 404 → No records found for the given user  
- **Comprehensive tests:** Implemented with `pytest` and `pytest-cov`.  
- **Expandable design:** Can be easily expanded to support date-range filtering or database storage.

## 🛠 Tech Stack

- Python 3
- FastAPI - Web Framework
- Pandas - Data Handling
- Uvicorn - ASGI Server (Local Development)

## 🧪 Testing & CI

- Pytest - Unit Testing
- Pytest-cov - Test Coverage Reports
- Httpx - FastAPI's TestClient for Endpoint Testing

## 🧠 Design Approach

- Used **FastAPI** for simplicity and performance.  
- **Pandas** efficiently handles large datasets (tested with 1M+ rows).  
- Data is stored in memory for prototype simplicity - can be upgraded to SQLite or PostgreSQL later.
- Focused on production-level clarity: descriptive docstrings, comments, and test coverage.

> **Note:** The current prototype focuses on `user_id` and `transaction_amount` columns. Additional fields (e.g. timestamps, categories) can be integrated in future iterations.

## 🏗️ Project Architecture

- `app/main.py` - Core FASTAPI application
- `tests/test_main.py` - Unit tests
- `sample.py` - Optional script to generate dummy_transactions.csv
- `requirements.txt` - Runtime dependencies
- `requirements-dev.txt` - Dev/test dependencies

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/DylanFernandes98/transaction-summary-api.git
   cd transaction-summary-api
   ```
2. **Create and activate a virtual environment**
- Windows (PowerShell)
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
- Mac/Linux (bash/zsh)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install dependencies**
- Runtime only (end users)
   ```bash
   pip install -r requirements.txt
- Development (for testing and linting)
   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
  
## 🧾 Example Usage

Once the server is running at [http://127.0.0.1:8000](http://127.0.0.1:8000):

1. **Health Check**
  ```bash
  curl http://127.0.0.1:8000/
  # {"message": "API is running"}
  ```
2. **Upload a CSV**
  ```bash
  curl.exe -X POST -F "file=@dummy_transactions.csv" http://127.0.0.1:8000/upload
  # {"message": "Successfully uploaded dummy_transactions.csv"}
  ```
3. **Get User Summary**
  ```bash
  curl http://127.0.0.1:8000/summary/1
  # {"user_id": 1, "min": 10, "max": 200, "mean": 105.25}
  ```





