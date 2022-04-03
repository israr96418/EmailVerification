from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQL_ALCHEMY_DATABASE_URL = "mysql+mysqldb://isrardawar:dawar96418@localhost:3306/uetm"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()