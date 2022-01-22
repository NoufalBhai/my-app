from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    author: UUID

class CreatePost(PostBase):
    pass

class ShowPost(PostBase):
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode=True
