import logging
logger = logging.getLogger(__name__)

import pytest

import fastauth
from fastauth import (
    EmailUserDatabase,
    EmailUser,
)

def test_register_login(caplog):
    caplog.set_level(logging.INFO)

    user_db = EmailUserDatabase(database_url='sqlite:///:memory:')
    user_db.migrate()

    user: EmailUser = user_db.create_user(email='hoge@example.com', password='hogehoge')

    # Password match logic
    user_db.authenticate(email='hoge@example.com', password='hogehoge')

    # Invalid password match logic
    with pytest.raises(EmailUserDatabase.InvalidPassword):
        user_db.authenticate(email='hoge@example.com', password='fugafuga')

    # User search logic
    with pytest.raises(EmailUserDatabase.UserNotFound):
        user_db.authenticate(email='fuga@example.com', password='')

    # Duplicated registration must not be allowed
    with pytest.raises(EmailUserDatabase.UserAlreadyExists):
        user_db.create_user(email='hoge@example.com', password='')

    # Email format validation logic
    with pytest.raises(EmailUserDatabase.EmailNotValid):
        user_db.create_user(email='hogehoge', password='')
