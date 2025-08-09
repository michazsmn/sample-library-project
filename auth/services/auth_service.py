from typing import Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from auth.models.token import TokenData
from auth.utils.auth_utils import get_hashed_password, verify_password
from pymongo_get_database import get_database
from user.services.user_service import get_user_by_email
from datetime import datetime, timedelta, timezone

# Secret key for signing JWT tokens.
SECRET_KEY = "W7lSpVhfhvd4ZOrzzTldEOIIesX7pHVTAA/S7Yszfis="

# Algorithm used for JWT token encoding
ALGORITHM = "HS256"

# OAuth2 password bearer flow for token retrieval
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_user(email: str, password: str, name: str, db = Depends(get_database)):
    if get_user_by_email(email, db):
        return None  # User already exists
    hashed_password = get_hashed_password(password)  # Assume this hashes the password
    user_data = {
        "email": email,
        "password": hashed_password,
        "name": name
    }
    user = db["users"].insert_one(user_data)  # Save user to the database
    return user

# Authentication function
def authenticate_user(email: str, password: str, db = Depends(get_database)):
    user = get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user

# Token generation function
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency for extracting and verifying JWT token
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db = Depends(get_database)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except jwt.InvalidTokenError:
        raise credentials_exception
    
    user = get_user_by_email(token_data.email, db)

    if user is None:
        raise credentials_exception
    
    return user

def get_current_active_user(current_user = Depends(get_current_user)):
    return current_user