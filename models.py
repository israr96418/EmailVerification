import uuid

from sqlalchemy import Column, String

from database import engine,Base
# Base = declarative_base()


class EmailSchedule(Base):
    __tablename__ = "emailschedule"
    id = Column(String(300), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(100), nullable=True)
    email_to = Column(String(100), nullable=False)
    message = Column(String(500), nullable=True)
    status = Column(String(200), nullable=True)