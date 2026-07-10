from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AI-Powered Bug Analyzer Service",
    description=(
        "Week 1 MVP for analyzing bugs, assigning severity, "
        "and recommending fixes."
    ),
    version="1.0.0",
)

app.include_router(router)