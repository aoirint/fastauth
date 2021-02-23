import os
import logging
logger = logging.getLogger(__name__)

from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from . import (
    EmailUserDatabase,
    EmailUser,
)

app = FastAPI()
db = EmailUserDatabase(
    database_url=os.environ.get('FASTAUTH_DATABASE', 'sqlite:///:memory:'),
)
db.migrate()


class AuthInfo(BaseModel):
    email: str
    password: str

@app.post('/register')
async def register(payload: AuthInfo, response: Response):
    try:
        user: EmailUser = db.create_user(email=payload.email, password=payload.password)
        return {
            'id': user.id,
            'email': user.email,
        }
    except EmailUserDatabase.EmailNotValid:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'error': 'Email format not valid' }
    except EmailUserDatabase.UserAlreadyExists:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'error': 'Email already registered' }

@app.post('/login')
async def login(payload: AuthInfo, response: Response):
    try:
        user: EmailUser = db.authenticate(email=payload.email, password=payload.password)
        return {
            'id': user.id,
            'email': user.email,
        }
    except EmailUserDatabase.EmailNotValid:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'error': 'Email format not valid' }
    except EmailUserDatabase.UserNotFound:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'error': 'No such user registered' }
    except EmailUserDatabase.InvalidPassword:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'error': 'Invalid Password' }
