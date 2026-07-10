# AI-Powered Bug Analyzer Service

An AI-inspired Bug Analyzer REST API built with **FastAPI** that analyzes software bug reports, assigns a severity level, identifies probable root causes, and recommends potential fixes.

> **Current Status:** Week 1 MVP (Heuristic-Based Analysis)

The current implementation uses a modular, rule-based heuristic engine to simulate AI-powered bug analysis. The project architecture has been intentionally designed so that the heuristic engine can later be replaced by an LLM (OpenAI, Gemini, Claude, etc.) with minimal changes to the API layer.

---

# Features

* AI-inspired bug analysis
* Automatic severity classification
* Probable root cause identification
* Actionable fix recommendations
* Architectural impact assessment
* Interactive Swagger UI documentation
* Modular FastAPI architecture
* Pydantic request and response validation
* Easily extensible heuristic engine
* Service-oriented backend structure

---

# Tech Stack

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

---

# Project Structure

```text
bug-analyzer/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── analyzer.py
│   │   └── heuristics.py
│   │
│   ├── services/
│   │   └── bug_service.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   └── utils/
│       └── constants.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Project Architecture

```
                    Client
                       │
                       ▼
               FastAPI Routes
                       │
                       ▼
             BugAnalysisService
                       │
                       ▼
                 BugAnalyzer
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
 Database Rule   Authentication   UI Rule
                      Rule
                       │
                       ▼
              BugAnalysisResponse
```

Each layer has a single responsibility, making the project easier to maintain, test, and extend.

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastapi uvicorn pydantic
```

---

# Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

Expected output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

# API Documentation

After the server starts successfully:

| Endpoint                    | Description         |
| --------------------------- | ------------------- |
| http://127.0.0.1:8000       | Health Check        |
| http://127.0.0.1:8000/docs  | Swagger UI          |
| http://127.0.0.1:8000/redoc | ReDoc Documentation |

---

# API Endpoints

## Health Check

**GET /**

Response

```json
{
  "status": "online",
  "message": "Bug Analyzer API is running.",
  "docs": "/docs"
}
```

---

## Analyze Bug Report

**POST /api/v1/analyze**

### Sample Request

```json
{
  "title": "Database connection timeout on login",
  "description": "Users are experiencing login failures due to database connection timeouts.",
  "logs": "ERROR connection pool exhausted",
  "stack_trace": "auth.py line 42",
  "component": "Authentication"
}
```

### Sample Response

```json
{
  "title": "Database connection timeout on login",
  "assigned_severity": "HIGH",
  "confidence_score": 0.91,
  "probable_root_causes": [
    "Connection pool exhaustion under heavy load.",
    "Missing database indexes on frequently queried fields."
  ],
  "recommended_fixes": [
    "Increase database connection pool size.",
    "Add indexes to frequently queried columns.",
    "Implement retry logic with exponential backoff."
  ],
  "architectural_impact": "Medium risk. Database bottlenecks may impact multiple dependent services."
}
```

---

# Bug Analysis Workflow

```
Bug Report
     │
     ▼
Request Validation
     │
     ▼
BugAnalysisService
     │
     ▼
BugAnalyzer
     │
     ▼
Execute Heuristic Rules
     │
     ▼
Generate Analysis
     │
     ▼
Return JSON Response
```

---

# Heuristic Rules

The current MVP uses keyword-based heuristics.

| Keywords                          | Assigned Severity |
| --------------------------------- | ----------------- |
| database, db, connection, timeout | HIGH              |
| login, auth, token, jwt           | CRITICAL          |
| ui, display, frontend, null       | LOW               |
| No matching rule                  | MEDIUM            |

Each heuristic is implemented independently, making the system easy to extend with additional rules.

---

# Design Principles

The project follows several software engineering best practices:

* Modular project architecture
* Separation of concerns
* Service layer pattern
* Single Responsibility Principle (SRP)
* Reusable heuristic engine
* Typed request and response models
* Easily replaceable analysis engine

---

# Future Roadmap

* LLM integration (OpenAI, Gemini, Claude)
* Persistent database storage
* Historical bug analysis
* Semantic search using vector databases
* User authentication
* Docker support
* CI/CD with GitHub Actions
* Unit testing with pytest
* Logging and monitoring
* Configuration management using environment variables

---

# Common Issues

## ModuleNotFoundError

Verify that you are running the server from the project root directory:

```bash
uvicorn app.main:app --reload
```

---

## Port Already in Use

Run the application on a different port:

```bash
uvicorn app.main:app --reload --port 8001
```

---

## Missing Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# License

This project is intended for educational, demonstration, and learning purposes.

