import pytest
from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_upload_valid_csv():
    """
    Uploads a valid CSV file and expects a success message.
    """
    
    # Mimics a tiny CSV file (1st line), and then create a temp in-memory file (2nd line)
    csv_content = "user_id,transaction_amount\n1,10\n1,20\n2,30\n" 
    file = io.BytesIO(csv_content.encode("utf-8"))

    # Simulate a file upload
    response = client.post("/upload", files={"file": ("data.csv", file, "text/csv")})
    
    # Verify a success response
    assert response.status_code == 200
    assert "Successfully uploaded data.csv" in response.json()["message"]

def test_upload_invalid_extension():
    """
    Rejects a non-CSV upload with a 400 error.
    """
    
    # Create a fake non-CSV file
    file = io.BytesIO(b"invalid content")

    # Simulate a file upload
    response = client.post("/upload", files={"file": ("data.txt", file, "text/plain")})

    # Verify correct error response
    assert response.status_code == 400
    assert response.json()["detail"] == "Please upload a CSV file."

def test_summary_valid_user():
    """
    Returns the correct summary stats for a valid user_id
    """

    # Mimics a tiny CSV file (1st line), and then create a temp in-memory file (2nd line)
    csv_content = "user_id,transaction_amount\n1,10\n1,20\n2,30\n" 
    file = io.BytesIO(csv_content.encode("utf-8"))

    # Simulate a file upload
    response = client.post("/upload", files={"file": ("data.csv", file, "text/csv")})

    # Request summary for user_id=1
    response = client.get("/summary/1")
    data = response.json()

    # Verify correct stats are returned
    assert response.status_code == 200
    assert data == {"user_id": 1, "min": 10, "max": 20, "mean": 15.00}