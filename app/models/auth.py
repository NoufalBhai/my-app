from typing import Optional
from pydantic import BaseModel, EmailStr

class Login(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    error: bool = True
    message: Optional[str]

class LoginSuccessResponse(LoginResponse):
    token: Optional[str]