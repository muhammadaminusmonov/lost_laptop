from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.models.models import Device

router = APIRouter(prefix="/devices", tags=["Devices"])


@router.get("/")
def get_devices(
    db: Session = Depends(get_db),
    name: Optional[str] = Query(None),
    status: Optional[bool] = Query(None),
    category: Optional[int] = Query(None),
    user_id: Optional[int] = Query(None),
):
    query = db.query(Device)

    if name:
        query = query.filter(Device.name.ilike(f"%{name}%"))

    if status is not None:
        query = query.filter(Device.status == status)

    if category:
        query = query.filter(Device.category == category)

    if user_id:
        query = query.filter(Device.user_id == user_id)

    return query.all()


@router.get("/{device_id}")
def get_device(device_id: int, db: Session = Depends(get_db)):
    return db.query(Device).filter(Device.id == device_id).first()