from fastapi import APIRouter

router = APIRouter(tags=["core"])


@router.get("/health")
def check_health():
    """Check if the system is healthy
    
    Mainly used by docker"""
    return {"status": "healthy"}
