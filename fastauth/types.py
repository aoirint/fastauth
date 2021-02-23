import uuid
from typing import NewType

UserId = NewType('UserId', uuid.UUID)
Email = NewType('Email', str)
HashedPassword = NewType('HashedPassword', str)
