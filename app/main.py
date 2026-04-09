from fastapi import FastAPI
from app.database import get_db,Base, engine
from app.routes import auth,task
from app import models,schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])