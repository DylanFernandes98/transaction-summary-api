"""
Author: Dylan Fernandes
Description:
A RESTful API built with FASTAPI that accepts CSV file uploads and returns summary statistics.
"""

# Import FASTAPI and related tools for building endpoints and handling file uploads
from fastapi import FastAPI, File, UploadFile, HTTPException
# Import pandas for reading and processing CSV data
import pandas as pd

# Create a FASTAPI application instance
app = FastAPI()

# Global variable to hold uploaded DataFrame
data = None

# Root endpoint
@app.get("/")
def home():
    """
    Returns a simple message confirming the API is running.
    """
    return {"message": "API is running"}

# File upload endpoint
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    """
    Accepts a CSV file upload and validates that it has the correct format.
    Returns a success message with the uploaded filename.
    """

    # Store globally for later access
    global data

    # Validation check
    if not file.filename or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")
    
    # Read CSV directly from uploaded file
    df = pd.read_csv(file.file)
    
    data = df

    # Return confirmation message if pass 
    return {"message": f"Successfully uploaded {file.filename}"}

# Summary statistics endpoint
@app.get("/summary/{user_id}")
def get_summary(user_id: int):
    """
    Returns summary statistics (min, max, mean)
    for a given user_id from the uploaded CSV data.
    """

    # Ensure data has been uploaded before generating summaries
    if data is None:
        raise HTTPException(status_code=400, detail="No data uploaded yet. Please use /upload first.")
    
    # Filter dataset for specified user_id
    user_data = data[data["user_id"] == user_id]

    # Handle case where no records exist for that user_id
    if user_data.empty:
        raise HTTPException(status_code=404, detail=f"No records found in user_id {user_id}.")
    
    # Store the summary statistics in a dictionary
    summary = {
        "user_id": user_id,
        "min": int(user_data["transaction_amount"].min()),
        "max": int(user_data["transaction_amount"].max()),
        "mean": float(round(user_data["transaction_amount"].mean(), 2)),
    }

    # Uncomment for debugging (optional)
    #print(user_data.head()) # Show first few records for inspection
    #print(user_data["transaction_amount"].describe()) #Display summary in console

    # Return results as JSON
    return summary