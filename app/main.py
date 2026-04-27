from fastapi import FastAPI
from app.api.v1 import user, device, category
from app.api.v1 import auth
from app.core.database import engine, Base
# from models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()
# url
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# include routers
app.include_router(user.router, prefix="/user")
app.include_router(device.router, prefix="/device")
app.include_router(category.router, prefix="/router")


@app.get("/")
def root():
    return {"message": "API is running"}