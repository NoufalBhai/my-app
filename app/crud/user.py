from sqlalchemy.orm.session import Session
from app.schemas import User
from werkzeug.security import generate_password_hash

def get_user_by_username(username: str, session: Session):
    try:
        user = session.query(User).where(User.username == username).one_or_none()
    except Exception:
        session.rollback()
        raise
    else:
        return user

def get_user_by_email(email: str, session: Session):
    try:
        user = session.query(User).where(User.email == email).one_or_none()
    except Exception:
        session.rollback()
        raise
    else:
        return user

def get_user_by_id(user_id: str, session: Session):
    try:
        user = session.query(User).where(User.id == user_id).one_or_none()
    except Exception:
        session.rollback()
        raise
    else:
        return user

def create_user(username:str, email: str, password: str, session: Session):
    try: 
        password = generate_password_hash(password)
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
    except Exception:
        session.rollback()
        raise
    else:
        return user