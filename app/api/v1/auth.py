from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)
from app.schemas.auth import (
    SignupRequest,
    LoginRequest,
    TokenResponse,
    RefreshRequest
)
from app.crud.user import create_user, get_user_by_email
from app.crud.refresh_token import (
    create_refresh_token as save_refresh_token,
    get_refresh_token,
    delete_refresh_token
)

router = APIRouter()

@router.post("/signup", response_model=TokenResponse)
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = hash_password(data.password)
    user = create_user(db, data.email, hashed)
    access = create_access_token({"user_id": user.id})
    refresh = create_refresh_token()
    save_refresh_token(db, user.id, refresh)
    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = create_access_token({"user_id": user.id})
    refresh = create_refresh_token()
    save_refresh_token(db, user.id, refresh)
    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }

@router.post("/refresh")
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):
    token = get_refresh_token(db, data.refresh_token)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    access = create_access_token({"user_id": token.user_id})
    return {
        "access_token": access
    }

@router.post("/logout")
def logout(data: RefreshRequest, db: Session = Depends(get_db)):
    delete_refresh_token(db, data.refresh_token)
    return {"message": "Logged out"}