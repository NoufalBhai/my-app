import json
from typing import List
from flask import Blueprint, jsonify
from app.db import SessionLocal
from app.models.post import CreatePost, ShowPost, ListPost, PostPage, UpdatePost
from app.crud.post import create_post, get_all_posts, get_single_post
from flask_pydantic import validate
from flask import Response

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
@validate()
def all_posts(query:PostPage):
    limit = query.limit
    page = query.page
    all_post = query.all_post
    offset = (page - 1) * limit
    posts = get_all_posts(session, limit=limit, offset = offset, all_data=all_post )
    if posts:
        post_list = ListPost.from_orm(posts).json()
        return  Response(post_list, mimetype='application/json')
    return {}, 404

@bp.get("/<post_id>")
def get_post(post_id: int):
    post = get_single_post(post_id, session)
    if post:
        return ShowPost.from_orm(post).dict()
    return {"error": True, "message": "Post Not Found"}, 404

@bp.put("/<post_id>")
@validate()
def update_post(post_id: int, body:UpdatePost):
    post = get_single_post(post_id, session)
    if not post:
        return {"error": True, "message": "Post Not Found"}, 404
    if not post.author == body.author:
        return {"error": True, "message": "You are not authorized to edit this post"}, 401
    if body.title:
        post.title = body.title
    if body.content:
        post.content = body.content
    try:
        session.commit()
        session.refresh(post)
    except Exception:
        session.rollback()
        raise
    else:
        return ShowPost.from_orm(post).dict()

    