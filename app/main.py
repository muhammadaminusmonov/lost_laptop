from fastapi import FastAPI




from app.api.v1 import auth

from app.core.database import engine, Base
# from models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])