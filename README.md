```python
import fastauth

fastauth.server(port=8000)
```

```sh
make makemigrations
make makemigrations FASTAUTH_DATABASE=sqlite:///db.sqlite3
FASTAUTH_DATABASE=sqlite:///db.sqlite3 make makemigrations

make migrate
make migrate FASTAUTH_DATABASE=sqlite:///db.sqlite3
FASTAUTH_DATABASE=sqlite:///db.sqlite3 make migrate
```


```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/register')
def register(email: str, password: str):
    pass

@app.get('/login')
def login(email: str, password: str):
    pass


from dataclasses import dataclass

@dataclass
class Server:
    host: str = '127.0.0.1'
    port: int = 8000

    def __post_init__(self):
        pass

    def start():
        pass
```
