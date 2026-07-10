from fastapi import APIRouter, HTTPException, status

from app.models.schemas import (
    BugAnalysisResponse,
    BugReportRequest,
)
from app.services.bug_service import BugAnalysisService

router = APIRouter(
    tags=["Bug Analyzer"],
)

bug_service = BugAnalysisService()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
)
async def health_check():
    """
    Simple endpoint to verify that the API is running.
    """

    return {
        "status": "online",
        "message": "Bug Analyzer API is running.",
        "docs": "/docs",
    }


@router.post(
    "/api/v1/analyze",
    response_model=BugAnalysisResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze a Bug Report",
    description="Analyze an incoming bug report and return severity, root causes, recommended fixes, and architectural impact.",
)
async def analyze_bug(
    bug: BugReportRequest,
) -> BugAnalysisResponse:
    """
    Analyze a bug report using the configured service layer.
    """

    try:
        return bug_service.analyze_bug(bug)

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Analysis failed: {str(exc)}",
        )