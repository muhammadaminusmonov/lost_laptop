from fastapi import FastAPI


from api.v1 import auth


from coree.database import engine, Base
from models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])