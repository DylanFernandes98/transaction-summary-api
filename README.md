# Suade Labs Technical Challenge

This project implements a RESTful API built with **FastAPI**. It processes uploaded CSV data and returns per-user transaction summary.  

The solution focuses on writing clean, maintainable, and testable code while following RESTful design principles. It demonstrates practical handling of file uploads, data validation, and how to get summary statistics using pandas.

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

## 🧠 Approach

- Used **FastAPI** for simplicity and performance.  
- **Pandas** efficiently handles large datasets (tested with 1M+ rows).  
- Data is held in memory (`global data`) for the challenge (suitable for a prototype), but in production this could potentially involve a database like SQLite.  
- Focused on production-level clarity: descriptive docstrings, comments, and test coverage.

> The challenge spec mentioned a “date range.”  
> This was consciously omitted to prioritise clarity, correctness, and testing within the 3 hour scope.  
> The feature could be added later using query parameters (e.g. `start_date`, `end_date`).

## 🏗️ Project Architecture

- `app/main.py` - Core FASTAPI application
- `tests/test_main.py` - Unit tests
- `sample.py` - Optional script to generate dummy_transactions.csv
- `requirements.txt` - Runtime dependencies
- `requirements-dev.txt` - Dev/test dependencies

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/DylanFernandes98/suade-api.git
   cd suade-api
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

