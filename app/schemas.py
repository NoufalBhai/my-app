from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from uuid import uuid4

from app.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "myapp"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    created_date = Column(DateTime, server_default=func.now(), nullable=False)
    updated_date = Column(DateTime, server_default=func.now(), server_onupdate=func.now(), nullable=False)

class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"schema": "myapp"}

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(UUID(as_uuid=True), ForeignKey(User.id, ondelete="CASCADE"))

    created_date = Column(DateTime, server_default=func.now(), nullable=False)
    updated_date = Column(DateTime, server_default=func.now(), server_onupdate=func.now(), nullable=False)

class Like(Base):
    __tablename__ = "likes"
    __table_args__ = {"schema": "myapp"}

    post_id = Column(Integer, ForeignKey(Post.id, ondelete="CASCADE"), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.id, ondelete="CASCADE"), primary_key=True)




