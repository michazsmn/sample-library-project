from pydantic import BaseModel

class RegisterModel(BaseModel):
    email: str
    password: str
    username: str

class LoginModel(BaseModel):
    email: str
    password: str