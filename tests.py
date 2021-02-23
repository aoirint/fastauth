import fastauth

def test_register_login():
    password = 'hogehoge'

    fastauth.register(password=password)

    login(password=password)
