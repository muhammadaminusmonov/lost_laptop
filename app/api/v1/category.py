from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.models.models import Category

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
def get_categories(
    db: Session = Depends(get_db),
    name: Optional[str] = Query(None),
    parent_id: Optional[int] = Query(None),
):
    query = db.query(Category)

    if name:
        query = query.filter(Category.name.ilike(f"%{name}%"))

    if parent_id is not None:
        query = query.filter(Category.parent_id == parent_id)

    return query.all()


@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    return db.query(Category).filter(Category.id == category_id).first()