from fastapi import FastAPI, Depends, BackgroundTasks
from pydantic import ValidationError
from sqlalchemy.orm import Session

import models
from database import get_db, engine
from models import Base
from schema import SendingEmailSchema
from send_email import send_email_in_background

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def getdata():
    return "hello"


@app.get("/send-email")
def Sending_email_background(background: BackgroundTasks, db: Session = Depends(get_db)):
    emails = db.query(models.EmailSchedule)
    for email in emails.all():
        try:
            send_email_in_background(background, email.title.upper(), email.email_to,
                                     {"title": email.title, "name": email.title})
        except ValidationError as Error:
            email.status = str(Error)
            db.commit()
            return str(Error)

        email.status = "Email send Successfully"
        db.commit()
        return {"messsage": "Email send Successfully"}


@app.post("/subscribe")
def EmialInQueue(data: SendingEmailSchema, db: Session = Depends(get_db)):
    data = models.EmailSchedule(**data.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message": "Email Add Successfully"}
