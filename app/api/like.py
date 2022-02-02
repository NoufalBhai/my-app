from uuid import UUID
from flask import Blueprint, session
from app.utils import auth
from app.crud.post import get_single_post
from app.crud.like import is_liked, like_post, unlike_post
from app.db import SessionLocal

bp = Blueprint("like", __name__, url_prefix="/like")

session = SessionLocal()


@bp.get("/<post_id>")
@auth.validate_token
def like_my_post(post_id:int, user_id: UUID):
    post = get_single_post(post_id, session)
    if not post:
        return {
            "error": True,
            "message": "Post Not Found"
        }, 404
    like = is_liked(user_id, post_id, session) 
    if like:
        unlike_post(like, session)
        return {
            "error": False,
            "message": "Post Disliked"
        }
    like_post(user_id, post_id, session)
    return {
        "error": False,
        "message": "Post Liked"
    }

    
