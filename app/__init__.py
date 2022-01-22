from flask import Flask
from app.schemas import Base

Base.metadata.create_all()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "fhcrt37yr8yr7ayr7ry37bctry78rt78rt378rtry7try89t7vy9ryyhr"
    )
    from app.api import user
    app.register_blueprint(user.bp)
    from app.api import post
    app.register_blueprint(post.bp)
    return app