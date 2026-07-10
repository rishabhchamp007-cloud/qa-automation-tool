from typing import Optional, Tuple, List

from app.utils.constants import (
    LOW,
    MEDIUM,
    HIGH,
    CRITICAL,
)

RuleResult = Optional[
    Tuple[
        str,            # Severity
        List[str],      # Root Causes
        List[str],      # Recommended Fixes
        str             # Architectural Impact
    ]
]


def database_rule(text: str) -> RuleResult:
    """
    Detect database and connection related issues.
    """

    keywords = [
        "database",
        "db",
        "connection",
        "postgres",
        "mysql",
        "sql",
        "query",
        "timeout",
    ]

    if not any(keyword in text for keyword in keywords):
        return None

    return (
        HIGH,
        [
            "Connection pool exhaustion under heavy load.",
            "Missing database indexes on frequently queried fields.",
        ],
        [
            "Increase database connection pool size.",
            "Add indexes to frequently queried columns.",
            "Implement retry logic with exponential backoff.",
        ],
        "Medium risk. Database bottlenecks may impact multiple dependent services.",
    )


def authentication_rule(text: str) -> RuleResult:
    """
    Detect authentication and authorization issues.
    """

    keywords = [
        "login",
        "auth",
        "token",
        "jwt",
        "oauth",
        "password",
        "authentication",
        "authorization",
    ]

    if not any(keyword in text for keyword in keywords):
        return None

    return (
        CRITICAL,
        [
            "Expired or invalid authentication tokens.",
            "Authentication middleware validation failure.",
            "Missing rate limiting on authentication endpoints.",
        ],
        [
            "Validate token generation and expiration logic.",
            "Review authentication middleware.",
            "Implement Redis-based rate limiting.",
        ],
        "High risk. Authentication failures can expose security vulnerabilities.",
    )


def ui_rule(text: str) -> RuleResult:
    """
    Detect frontend/UI related issues.
    """

    keywords = [
        "ui",
        "display",
        "frontend",
        "null",
        "undefined",
        "css",
        "button",
        "screen",
    ]

    if not any(keyword in text for keyword in keywords):
        return None

    return (
        LOW,
        [
            "Frontend attempted to access a null object.",
            "Unexpected API response structure.",
        ],
        [
            "Add optional chaining.",
            "Validate API responses before rendering.",
            "Provide default values for missing fields.",
        ],
        "Low risk. Primarily affects user experience.",
    )


def default_rule() -> RuleResult:
    """
    Default fallback when no heuristic matches.
    """

    return (
        MEDIUM,
        [
            "Unhandled edge case in business logic.",
        ],
        [
            "Add defensive validation.",
            "Increase logging around the affected module.",
            "Write additional unit tests.",
        ],
        "Low risk. Appears isolated to the reported component.",
    )