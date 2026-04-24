from fastapi import APIRouter
from backend.engine import analyze

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/detect")
def detect(payload: dict):
    return analyze(payload)