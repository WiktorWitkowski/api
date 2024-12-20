"""Main FastApi file."""
from fastapi import FastAPI
from sqlmodel import SQLModel
from crud import router
from deps import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()
app.include_router(router=router, prefix="/v1")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/check_health")
def check_health():
    return {"API": "Up and Running!"}