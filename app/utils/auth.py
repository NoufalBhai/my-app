from functools import wraps
from flask import request
from jose import jwt
from jose.exceptions import JWTError

secrect_key = "hgdfys67rfter67etd76yfwgf7g7w6egfgw6gf7c7wbyg76 wgte76rte7tfr7etw76"

def validate_token(fun):
    @wraps(fun)
    def deco(*args, **kwargs):
        headers = request.headers
        if not "Authorization" in headers:
            return {
                "error": True,
                "message": "Authorization needed"
            }, 400
        
        bearer_token = headers.get("Authorization")
        if not bearer_token.startswith("Bearer"):
            return {
                "error": True,
                "message": "Incorrect Authorization Format"
            }, 400
        token = bearer_token.split(" ")[-1]
        try:
            user_data = jwt.decode(token, secrect_key)
        except JWTError:
            return {
                "error": True,
                "message": "Authorization Failed"
            }, 401
        kwargs.update({"user_id": user_data.get("user_id")})
        return fun(*args, **kwargs)
    return deco
