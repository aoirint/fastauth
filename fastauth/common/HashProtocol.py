from typing import Protocol

class HashProtocol(Protocol):
    def hash(self, secret: str):
        pass

    def verify(self, secret: str, hash: str) -> str:
        pass
