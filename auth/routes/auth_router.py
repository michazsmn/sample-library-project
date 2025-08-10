from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from auth.models.token import Token
from auth.services.auth_service import authenticate_user, create_access_token, create_user
from pymongo_get_database import get_database
from user.models.authmodels import RegisterModel, LoginModel


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post("/token")
async def login_for_access_token(loginmodel : LoginModel) -> Token:
    db = Depends(get_database)
    user = authenticate_user(loginmodel.email, loginmodel.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["email"]},
        expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")

@auth_router.post("/register")
async def register_user(registermodel : RegisterModel):
    db = Depends(get_database)
    user = create_user(registermodel.email, registermodel.password, registermodel.username, db)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="User already exists",
        )
    return {"message": "User created successfully", "user_id": str(user.inserted_id)}

