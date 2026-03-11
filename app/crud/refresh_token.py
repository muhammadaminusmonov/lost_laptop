from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.refresh_token import RefreshToken


def create_refresh_token(db: Session, user_id: int, token: str):
    expires = datetime.utcnow() + timedelta(days=30)
    db_token = RefreshToken(
        user_id=user_id,
        token=token,
        expires_at=expires
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def get_refresh_token(db: Session, token: str):
    return db.query(RefreshToken).filter(
        RefreshToken.token == token
    ).first()


def delete_refresh_token(db: Session, token: str):
    db.query(RefreshToken).filter(
        RefreshToken.token == token
    ).delete()
    db.commit()