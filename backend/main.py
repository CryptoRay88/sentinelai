from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="SentinelAI")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "SentinelAI active"}