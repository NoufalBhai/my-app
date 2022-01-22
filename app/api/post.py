from typing import List
from flask import Blueprint
from app.db import SessionLocal
from app.models.post import CreatePost, ShowPost
from app.crud.post import create_post, get_all_posts, get_single_post
from flask_pydantic import validate
from pydantic import parse_obj_as

session = SessionLocal()

bp = Blueprint("post", __name__, url_prefix="/post")

@bp.post("/")
@validate()
def post_creation(body: CreatePost):
    post = create_post(body, session)
    if post:
        return ShowPost.from_orm(post).dict(), 201
    return {
        "error": True,
        "message": "Something went wrong"
    }, 500

@bp.get("/")
def all_posts():
    posts = get_all_posts(session)
    if posts:
        post_list = [ShowPost.from_orm(post).dict() for post in posts]
        return {"posts": post_list}
    return {}, 404