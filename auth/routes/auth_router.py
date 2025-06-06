from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from auth.models.token import Token
from auth.services.auth_service import authenticate_user, create_access_token
from pymongo_get_database import get_database


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

auth_router.post("/token")
async def login_for_access_token(
        form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
        db = Depends(get_database)
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
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