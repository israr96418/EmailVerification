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

sqlalchemy_database_url = f"mysql+mysqldb://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_portNumber}/{setting.database_name}"


# create engine are responsible to connect fastapi with your database through url

engine = create_engine(sqlalchemy_database_url)

# sessionmaker are responsible to make conversation/communication with the database
# the sessionmaker can provide a factory for Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this ftn are responsible to convert all the model into table in databass
# when we run the server again and again  it all time model will be converted into tables
# this function also prevent to create the table again and again
Base = declarative_base()


engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
