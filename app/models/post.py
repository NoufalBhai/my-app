from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    author: UUID

class CreatePost(PostBase):
    pass

class ShowPost(PostBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode=True

class ListPost(BaseModel):
    __root__: List[ShowPost]

    class Config:
        orm_mode=True

class PostPage(BaseModel):
    limit: Optional[int] = 3
    page: Optional[int] = 1
    all_post: Optional[bool] = False

class UpdatePost(BaseModel):
    title: Optional[str]
    content: Optional[str]
    author: UUID

class DeletePost(BaseModel):
    author: UUID
