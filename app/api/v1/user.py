from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.models.models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(
    db: Session = Depends(get_db),
    username: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
):
    query = db.query(User)

    if username:
        query = query.filter(User.username.ilike(f"%{username}%"))

    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))

    return query.all()


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()