# fastauth

```sh
make makemigrations
make makemigrations FASTAUTH_DATABASE=sqlite:///db.sqlite3
FASTAUTH_DATABASE=sqlite:///db.sqlite3 make makemigrations

make migrate
make migrate FASTAUTH_DATABASE=sqlite:///db.sqlite3
FASTAUTH_DATABASE=sqlite:///db.sqlite3 make migrate
```

## TODO
```python
import fastauth

fastauth.server(port=8000)
```
