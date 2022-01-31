from email import message
from flask import Blueprint
from werkzeug.security import check_password_hash
from flask_pydantic import validate
from jose import jwt

from app.models.auth import Login, LoginResponse, LoginSuccessResponse
from app.crud.user import get_user_by_email
from app.db import SessionLocal

session = SessionLocal()
secrect_key = "hgdfys67rfter67etd76yfwgf7g7w6egfgw6gf7c7wbyg76 wgte76rte7tfr7etw76"

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.post("/login")
@validate()
def login(body: Login):
    user = get_user_by_email(body.email, session)
    if not user:
        return LoginResponse(message="User Not Found").dict(), 404
    
    is_correct_password = check_password_hash(user.password, body.password)
    if not is_correct_password:
        return LoginResponse(message="email or password incorrect").dict(), 403
    user_data = {
        "user_id": str(user.id),
        "username": user.username
    }
    token = jwt.encode(user_data, secrect_key)
    return LoginSuccessResponse(error=False, message="Login Success", token=token).dict()