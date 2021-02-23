```python
import fastauth

fastauth.server(port=8000)
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
