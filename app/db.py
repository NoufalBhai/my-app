from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

DATABASE_URL = "postgresql://postgres:password@localhost:5432/my-app"

engine = create_engine(DATABASE_URL)

Base = declarative_base(bind=engine)

SessionLocal = sessionmaker(bind=engine)

