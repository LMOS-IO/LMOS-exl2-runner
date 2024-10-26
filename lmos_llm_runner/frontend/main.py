"""This file defines the fastAPI ASGI app"""

from fastapi import FastAPI

from .router import router as CompletionsRouter
from .core import router as CoreRouter

__all__ = ["app"]

app = FastAPI(
    title="LLM Runner",
    description="LLM Runner for LMOS ecosystem",
)

app.include_router(CompletionsRouter)
app.include_router(CoreRouter)
