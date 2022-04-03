import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

load_dotenv(".env")


class Envs:
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: EmailStr = os.getenv("MAIL_FROM")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")


config = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_TLS=True,
    MAIL_SSL=False,
    MAIL_DEBUG=True,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
)


def send_email_in_background(background: BackgroundTasks, subject: str, email_to: EmailStr, body: dict):
    template =f"""
    <html>
    <body>
    <h1 style="color:red;">hi</h1>
    </body>
    </html>
"""
    message = MessageSchema(
        subject="EasyShop Verification Main",
        recipients=[email_to],
        body=template,
        subtype='html'
    )
    fm = FastMail(config)
    background.add_task(
        fm.send_message, message,template_name="email.html"
    )
