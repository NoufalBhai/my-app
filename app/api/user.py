from email import message
from flask import Blueprint
from flask_pydantic import validate
from app.models.user import CreateUser, ShowUser
from app.crud.user import get_user_by_email, get_user_by_username, get_user_by_id, create_user
from app.db import SessionLocal

session = SessionLocal()

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.post("/")
@validate()
def user_creation(body: CreateUser):
    if get_user_by_username(body.username, session):
        return {
            "error": True,
            "message": f"Username {body.username} already exist"
        }, 400
    if get_user_by_email(body.email, session):
        return {
            "error": True,
            "message": f"Email {body.email} already exist"
        }, 400
    
    new_user = create_user(**body.dict(), session=session)
    return ShowUser.from_orm(new_user).dict(), 201
