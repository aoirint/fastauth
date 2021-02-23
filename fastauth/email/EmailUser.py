from peewee import (
    Model,
    UUIDField,
    CharField,
)
from playhouse.hybrid import hybrid_property

import uuid
import typing

from .types import (
    UserId,
    Email,
    HashedPassword,
)

class EmailUser(Model):
    _id = UUIDField(column_name='id', primary_key=True, default=uuid.uuid4)
    _email = CharField(column_name='email', max_length=255, unique=True)
    _password = CharField(column_name='password', max_length=255)


    @hybrid_property
    def id(self) -> UserId:
        return typing.cast(UserId, self._id)

    @id.setter
    def set_id(self, id: uuid.UUID):
        self._id = typing.cast(uuid.UUID, id)


    @hybrid_property
    def email(self) -> Email:
        return typing.cast(Email, self._email)

    @email.setter
    def set_email(self, email: Email):
        self._email = typing.cast(str, email)


    @hybrid_property
    def password(self) -> HashedPassword:
        return typing.cast(HashedPassword, self._password)

    @password.setter
    def set_password(self, password: HashedPassword):
        self._password = typing.cast(str, password)

    class Meta:
        table_name = 'fastauth_emailuser'
