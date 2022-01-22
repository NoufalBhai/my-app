from uuid import UUID
from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    username: str
    email: EmailStr

class CreateUser(BaseUser):
    password: str

class ShowUser(BaseUser):
    id: UUID

    class Config:
        orm_mode=True