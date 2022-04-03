import uuid

from sqlalchemy import Column, String, Table, MetaData
# from sqlalchemy.ext.declarative import declarative_base

from database import engine,Base
# Base = declarative_base()


class EmailSchedule(Base):
    __tablename__ = "emailschedule"
    id = Column(String(300), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(100), nullable=True)
    email_to = Column(String(100), nullable=False)
    message = Column(String(500), nullable=True)
    status = Column(String(200), nullable=True)

    # def __init__(self, title, email_to, message, status):
    #     self.id = str(uuid.uuid4().hex)
    #     self.title = title
    #     self.email_to = email_to
    #     self.message = message
    #     self.status = status

# Base.metadata.create_all(engine)