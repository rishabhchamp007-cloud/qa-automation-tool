import random

from app.core.heuristics import (
    authentication_rule,
    database_rule,
    default_rule,
    ui_rule,
)
from app.models.schemas import (
    BugAnalysisResponse,
    BugReportRequest,
)
from app.utils.constants import (
    MAX_CONFIDENCE,
    MIN_CONFIDENCE,
)


class BugAnalyzer:
    """
    Coordinates bug analysis by applying heuristic rules
    and constructing a standardized response.
    """

    def __init__(self):
        self.rules = [
            database_rule,
            authentication_rule,
            ui_rule,
        ]

    @staticmethod
    def _prepare_text(bug: BugReportRequest) -> str:
        """
        Combine relevant bug fields into a single searchable string.
        """

        return " ".join(
            filter(
                None,
                [
                    bug.title,
                    bug.description,
                    bug.logs,
                    bug.stack_trace,
                    bug.component,
                ],
            )
        ).lower()

    @staticmethod
    def _generate_confidence() -> float:
        """
        Generate a confidence score for heuristic analysis.
        """

        return round(
            random.uniform(
                MIN_CONFIDENCE,
                MAX_CONFIDENCE,
            ),
            2,
        )

    def analyze(
        self,
        bug: BugReportRequest,
    ) -> BugAnalysisResponse:
        """
        Analyze the incoming bug report using the configured
        heuristic rules.
        """

        text = self._prepare_text(bug)

        for rule in self.rules:

            result = rule(text)

            if result:

                (
                    severity,
                    root_causes,
                    fixes,
                    impact,
                ) = result

                return BugAnalysisResponse(
                    title=bug.title,
                    assigned_severity=severity,
                    confidence_score=self._generate_confidence(),
                    probable_root_causes=root_causes,
                    recommended_fixes=fixes,
                    architectural_impact=impact,
                )

        severity, root_causes, fixes, impact = default_rule()

        return BugAnalysisResponse(
            title=bug.title,
            assigned_severity=severity,
            confidence_score=self._generate_confidence(),
            probable_root_causes=root_causes,
            recommended_fixes=fixes,
            architectural_impact=impact,
        )