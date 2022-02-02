from uuid import UUID
from sqlalchemy.orm.session import Session
from app.schemas import Like

def is_liked(user_id: UUID, post_id: int, session: Session):
    try:
        liked = session.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).one_or_none()
    except Exception:
        session.rollback()
        raise
    else:
        return liked

def like_post(user_id: UUID, post_id: int, session: Session):
    try:
        like = Like(user_id=user_id, post_id=post_id)
        session.add(like)
        session.commit()
    except Exception:
        session.rollback()
        raise
    else:
        return like

def unlike_post(like: Like, session: Session):
    try:
        session.delete(like)
        session.commit()
    except Exception:
        session.rollback()
        raise
    else:
        return like
