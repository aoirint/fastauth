from dataclasses import dataclass
from typing import Optional
from .types import Email, Password

import peewee

@dataclass
class EmailUser(peewee.Model):
    id = peewee.UUIDField()
    email: peewee.Email
    password: Password

    @staticmethod
    def authenticate(email: Email, password: Password) -> EmailUser:
        try:
            user: Optional[EmailUser] = EmailUser.objects.get(email=email)
            assert user is not None
        except EmailUser.DoesNotExist:
            raise UserNotFound(email=email, password=password)

        if user.password != password:
            raise InvalidPassword(email=email, password=password)

        return user


@dataclass
class UserException(Exception):
    email: Email
    password: Password

@dataclass
class UserNotFound(UserException):
    pass

@dataclass
class InvalidPassword(UserException):
    pass
