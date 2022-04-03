from pydantic import BaseModel


class SendingEmailSchema(BaseModel):
    title: str
    email_to: str
    message:str

    class Config:
        orm_mode = True