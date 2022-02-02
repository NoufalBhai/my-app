from uuid import UUID
from app.schemas import Post
from sqlalchemy.orm.session import Session
from app.models.post import CreatePost

def create_post(post: CreatePost, user_id: UUID, session: Session):
    try:
        post = Post(**post.dict(), author=user_id)
        session.add(post)
        session.commit()
        session.refresh(post)
    except Exception:
        session.rollback()
        raise
    else:
        return post

def get_all_posts(session:Session, limit:int = 3, offset:int = 0, all_data: bool = False):
    try: 
        posts = session.query(Post)
        if not all_data:
            posts = posts.limit(limit).offset(offset)
        all_posts = posts.all()
    except Exception:
        session.rollback()
        raise
    else:
        return all_posts

def get_single_post(post_id: int, session: Session):
    try: 
        post = session.query(Post).where(Post.id == post_id).one_or_none()
    except Exception:
        session.rollback()
        raise
    else:
        return post