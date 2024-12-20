"""Main FastApi file."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/check_health")
def check_health():
    return {"API": "Up and Running!"}