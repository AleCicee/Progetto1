UTENTI = {admin : 123}
def login(username,password):
    print("Login function called")
    if username in UTENTI and UTENTI[username] == password:
        return True
    else:
        return False

def signin(username,password):
    if username in UTENTI:
        return False
    else:
        UTENTI[username] = password
        return True