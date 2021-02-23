from peewee import (
    Database,
    IntegrityError,
)
from playhouse.db_url import connect
from peewee_migrate import Router

from passlib.hash import (
    pbkdf2_sha256,
)
from email_validator import (
    validate_email,
    EmailNotValidError,
    ValidatedEmail,
)

from pathlib import Path
from dataclasses import dataclass, field
import typing
from typing import Optional

from .EmailUser import EmailUser
from .types import (
    UserId,
    Email,
    HashedPassword,
)
from ..HashProtocol import HashProtocol

import logging
logger = logging.getLogger(__name__)


SCRIPT_DIR = Path(__file__).parent
MIGRATE_DIR = SCRIPT_DIR / 'migrations'


@dataclass
class EmailUserDatabase:
    database_url: str
    database: Database = field(init=False)
    hash: HashProtocol = pbkdf2_sha256

    def __post_init__(self):
        assert self.database_url is not None
        self.database = connect(self.database_url)

    def _create_user(self, email: Email, password: HashedPassword) -> EmailUser:
        return EmailUser.create(email=typing.cast(str, email), password=typing.cast(str, password))

    def _get_user(self, email: Email) -> EmailUser:
        return EmailUser.get(email=email)

    def _verify_password(self, secret: str, hash: HashedPassword):
        return self.hash.verify(secret=secret, hash=typing.cast(str, hash))


    def create_user(self, email: str, password: str) -> EmailUser:
        logger.info(f'User registering with email {email}')

        try:
            _validated_email: ValidatedEmail = validate_email(email)
        except EmailNotValidError:
            raise EmailUserDatabase.EmailNotValid()
        validated_email: Email = typing.cast(Email, _validated_email.email)

        hashed_password = typing.cast(HashedPassword, self.hash.hash(password))

        with EmailUser.bind_ctx(self.database):
            try:
                user: EmailUser = self._create_user(
                    email=validated_email,
                    password=hashed_password,
                )
                assert user is not None
            except IntegrityError:
                raise EmailUserDatabase.UserAlreadyExists()

            logger.info(f'User registered with email {email}: {user.id}')
            return user


    def authenticate(self, email: str, password: str) -> EmailUser:
        try:
            _validated_email: ValidatedEmail = validate_email(email)
        except EmailNotValidError:
            raise EmailUserDatabase.EmailNotValid()
        validated_email: Email = typing.cast(Email, _validated_email.email)

        with EmailUser.bind_ctx(database=self.database):
            try:
                user: Optional[EmailUser] = self._get_user(email=validated_email)
                assert user is not None
            except EmailUser.DoesNotExist:
                raise EmailUserDatabase.UserNotFound()

            if not self._verify_password(password, user.password):
                raise EmailUserDatabase.InvalidPassword()

            return user


    def migrate(self):
        router = Router(database=self.database, migrate_dir=MIGRATE_DIR)
        router.run()


    @dataclass
    class UserException(Exception):
        pass

    @dataclass
    class EmailNotValid(UserException):
        pass

    @dataclass
    class UserAlreadyExists(UserException):
        pass

    @dataclass
    class UserNotFound(UserException):
        pass

    @dataclass
    class InvalidPassword(UserException):
        pass
