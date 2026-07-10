# AI-Powered Bug Analyzer Service

An AI-inspired Bug Analyzer API built using **FastAPI**. This project analyzes software bug reports, assigns a severity level, identifies probable root causes, and recommends possible fixes.

> **Current Status:** Week 1 MVP (Heuristic-Based Analysis)

The current implementation uses rule-based heuristics to simulate AI-powered bug analysis. The architecture is designed so that the analysis engine can later be replaced with an actual LLM (OpenAI, Claude, Gemini, etc.) without changing the API.

---

## Features

- Analyze software bug reports
- Automatic bug severity classification
- Probable root cause identification
- Recommended fixes
- Architectural impact assessment
- Interactive Swagger API documentation
- Structured request and response validation using Pydantic

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## Project Structure

```
project/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

---

### 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

or

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the development server using:

```bash
uvicorn main:app --reload
```

If your file has a different name, replace **main** with the filename.

Example

If the file is named

```
bug_service.py
```

then run

```bash
uvicorn bug_service:app --reload
```

---

## Expected Output

After starting successfully, the terminal should display something similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## Accessing the API

### Root Endpoint

Open:

```
http://127.0.0.1:8000/
```

Expected response:

```json
{
    "status": "online",
    "message": "Bug Analyzer API is running. Go to /docs for Swagger UI."
}
```

---

### Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test the API directly from your browser.

Available endpoints:

- GET /
- POST /api/v1/analyze

---

## Sample Request

POST

```
/api/v1/analyze
```

Request Body

```json
{
  "title": "Database connection timeout on login",
  "description": "Users are facing 504 gateway timeouts during login.",
  "logs": "Connection pool exhausted",
  "stack_trace": "auth.py line 42",
  "component": "Authentication"
}
```

---

## Sample Response

```json
{
  "title": "Database connection timeout on login",
  "assigned_severity": "HIGH",
  "confidence_score": 0.91,
  "probable_root_causes": [
    "Connection pool exhaustion under heavy load.",
    "Missing database index on frequently queried lookup keys."
  ],
  "recommended_fixes": [
    "Increase the maximum pool size.",
    "Implement retry with exponential backoff."
  ],
  "architectural_impact": "Medium risk. Could slow down adjacent services."
}
```

---

## Bug Analysis Logic

The MVP currently uses simple keyword-based heuristics.

Examples:

| Keyword | Severity |
|----------|----------|
| database, db, connection | HIGH |
| login, auth, token | CRITICAL |
| ui, display, null | LOW |
| Others | MEDIUM |

This logic can later be replaced by an AI model or LLM without changing the API interface.

---

## API Workflow

```
Client
   │
   ▼
POST Request
   │
   ▼
FastAPI
   │
   ▼
Pydantic Validation
   │
   ▼
Bug Analysis Engine
   │
   ▼
Generate Response
   │
   ▼
Return JSON
```

---

## Common Issues

### ModuleNotFoundError

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

### Port Already in Use

Run on another port:

```bash
uvicorn main:app --reload --port 8001
```

---

### 404 Not Found

Verify that you are visiting:

```
http://127.0.0.1:8000/
```

or

```
http://127.0.0.1:8000/docs
```

---

### File Name Error

If your application file is not named `main.py`, update the command accordingly.

Example:

```bash
uvicorn app:app --reload
```

where

```
app.py
```

contains

```python
app = FastAPI()
```

---

## Future Improvements

- OpenAI / Gemini integration
- LLM-powered bug reasoning
- Vector database for historical bug search
- Authentication
- Database integration
- Bug history tracking
- CI/CD pipeline
- Docker support
- Unit and integration tests

---

## License

This project is intended for educational and demonstration purposes.