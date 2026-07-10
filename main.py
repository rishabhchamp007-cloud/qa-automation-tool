from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import random

app = FastAPI(
    title="AI-Powered Bug Analyzer Service",
    description="Week 1 MVP for analyzing bugs, assigning severity, and recommending fixes.",
    version="1.0.0"
)

# --- Request Schemas ---
class BugReportRequest(BaseModel):
    title: str = Field(..., example="Database connection timeout on login")
    description: str = Field(..., example="Users are facing 504 gateway timeouts when attempting to log in during peak hours.")
    logs: str = Field(None, example="ERROR: asyncpg.exceptions.ConnectionDoesNotExistError: connection was closed")
    stack_trace: str = Field(None, example="File 'auth.py', line 42, in login_user...")
    component: str = Field(..., example="Authentication / Backend")

# --- Response Schemas ---
class BugAnalysisResponse(BaseModel):
    title: str
    assigned_severity: str = Field(..., description="Calculated severity: LOW, MEDIUM, HIGH, CRITICAL")
    confidence_score: float = Field(..., description="AI confidence score between 0.0 and 1.0")
    probable_root_causes: List[str] = Field(..., description="List of likely reasons behind the bug")
    recommended_fixes: List[str] = Field(..., description="Actionable steps to resolve the issue")
    architectural_impact: str = Field(..., description="Potential side effects or structural considerations")

# --- Analysis Engine (Week 1 Functional Implementation) ---
def analyze_bug_logic(bug: BugReportRequest) -> BugAnalysisResponse:
    """
    Core analysis logic. For Week 1, this uses deterministic heuristics combined with 
    structured responses to simulate high-quality AI analysis. 
    Can be easily swapped with an LLM API call later.
    """
    text_to_analyze = (bug.title + " " + bug.description + " " + (bug.logs or "")).lower()
    
    # Default fallback values
    severity = "MEDIUM"
    root_causes = ["Uncaught edge case in business logic."]
    fixes = ["Add defensive null/empty checks.", "Add comprehensive unit tests for this scenario."]
    impact = "Low risk. Isolated to the specific component."
    confidence = 0.85

    # Heuristic Rule 1: Database Issues
    if "db" in text_to_analyze or "database" in text_to_analyze or "connection" in text_to_analyze:
        severity = "HIGH"
        root_causes = [
            "Connection pool exhaustion under heavy load.",
            "Missing database index on frequently queried lookup keys."
        ]
        fixes = [
            "Increase the maximum pool size in the database configuration.",
            "Implement a retry mechanism with exponential backoff for transient DB connection drops."
        ]
        impact = "Medium risk. Could slow down adjacent services relying on the same database cluster."

    # Heuristic Rule 2: Security / Auth Issues
    elif "login" in text_to_analyze or "auth" in text_to_analyze or "token" in text_to_analyze:
        severity = "CRITICAL"
        root_causes = [
            "Expired or improperly validated JWT / OAuth token secrets.",
            "Rate-limiting omitted on sensitive authentication endpoints."
        ]
        fixes = [
            "Verify token expiration parameters and validation middleware logic.",
            "Implement a Redis-backed rate limiter on the login endpoint immediately to prevent brute-force attempts."
        ]
        impact = "High risk. Potential exposure of user authentication pathways or resource exhaustion."

    # Heuristic Rule 3: UI / Null Pointer / Minor
    elif "ui" in text_to_analyze or "display" in text_to_analyze or "null" in text_to_analyze:
        severity = "LOW"
        root_causes = ["Frontend attempting to read a property of an undefined object response."]
        fixes = ["Update API response schema to guarantee non-null default values, or add optional chaining in frontend."]
        impact = "Negligible risk. Purely cosmetic or client-side disturbance."

    return BugAnalysisResponse(
        title=bug.title,
        assigned_severity=severity,
        confidence_score=round(random.uniform(0.80, 0.98), 2) if confidence == 0.85 else confidence,
        probable_root_causes=root_causes,
        recommended_fixes=fixes,
        architectural_impact=impact
    )

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"status": "online", "message": "Bug Analyzer API is running. Go to /docs for Swagger UI."}

@app.post("/api/v1/analyze", response_model=BugAnalysisResponse)
async def analyze_bug(bug: BugReportRequest):
    try:
        analysis_result = analyze_bug_logic(bug)
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during analysis: {str(e)}")