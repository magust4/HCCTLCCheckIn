# HCCTLC Student Check-In App

A simple web app that allows students to check in using their student ID. This helps the department track usage of services and space more effectively.

---

## How to Run the App

### 1. Install required Python libraries

```bash
pip install fastapi uvicorn pandas openpyxl
```

---

### 2. Run the FastAPI backend server

```bash
uvicorn backend.app:app --reload
```

This will start the API at `http://localhost:8000`.

---

### 3. Open the frontend

> ⚠Browsers may block fetch requests if you open the HTML file directly via `file://`. It's best to serve the frontend with a local server.

#### Option A — Open directly (may fail on fetch):

**MacOS:**
```bash
open frontend/index/index.html
```

**Windows:**
```bash
start frontend\index\index.html
```

#### Option B — Recommended: Run a local web server

```bash
cd frontend
python -m http.server 3000
```

Then open this URL in your browser:
```
http://localhost:3000/index/index.html
```

---

## Features

- Numeric keypad check-in
- 7-digit student ID validation
- Writes check-in data to Excel (`StudentResponses.xlsx`)
- Uses FastAPI + Pandas backend

---

## Project Structure

```
project-root/
├── backend/
│   └── app.py
│   └── StudentResponses.xlsx
└── frontend/
    ├── index/
    │   └── index.html
    │   └── script.js
    └── hcctlc/
        └── hcctlc.html
```


