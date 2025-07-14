from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing only, restrict in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the absolute path to this script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, "StudentResponses.xlsx")
TABLE_SHEET = "Sheet1"

class ResponseData(BaseModel):
    date: date  # expects YYYY-MM-DD format
    studentId: str
    selectedOption: str

def append_to_excel(data: ResponseData):
    new_row = pd.DataFrame([{
        "date": data.date.isoformat(),
        "studentId": data.studentId,
        "selectedOption": data.selectedOption
    }])

    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE, sheet_name=TABLE_SHEET)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_excel(EXCEL_FILE, sheet_name=TABLE_SHEET, index=False)

@app.post("/submit")
async def submit_response(response: ResponseData):
    try:
        append_to_excel(response)
        return {"message": "Data saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
