from typing import List, Optional

from pydantic import BaseModel, Field


class BugReportRequest(BaseModel):
    """
    Request payload received from the client.
    """

    title: str = Field(
        ...,
        example="Database connection timeout on login",
    )

    description: str = Field(
        ...,
        example=(
            "Users are facing 504 gateway timeouts "
            "when attempting to log in."
        ),
    )

    logs: Optional[str] = Field(
        default=None,
        example="ERROR: asyncpg.exceptions.ConnectionDoesNotExistError",
    )

    stack_trace: Optional[str] = Field(
        default=None,
        example="File 'auth.py', line 42...",
    )

    component: str = Field(
        ...,
        example="Authentication / Backend",
    )


class BugAnalysisResponse(BaseModel):
    """
    Standard response returned after analysis.
    """

    title: str

    assigned_severity: str = Field(
        ...,
        description="LOW | MEDIUM | HIGH | CRITICAL",
    )

    confidence_score: float = Field(
        ...,
        description="Confidence score between 0.0 and 1.0",
    )

    probable_root_causes: List[str]

    recommended_fixes: List[str]

    architectural_impact: str