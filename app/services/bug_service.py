from app.core.analyzer import BugAnalyzer
from app.models.schemas import (
    BugAnalysisResponse,
    BugReportRequest,
)


class BugAnalysisService:
    """
    Service layer responsible for coordinating
    bug analysis operations.

    Future responsibilities may include:
    - Database operations
    - AI/LLM integration
    - Logging
    - Caching
    - Audit history
    """

    def __init__(self) -> None:
        self.analyzer = BugAnalyzer()

    def analyze_bug(
        self,
        bug: BugReportRequest,
    ) -> BugAnalysisResponse:
        """
        Analyze a bug report.

        Parameters
        ----------
        bug : BugReportRequest
            Incoming bug report.

        Returns
        -------
        BugAnalysisResponse
            Structured analysis result.
        """

        return self.analyzer.analyze(bug)