UTENTI = {}
def login(username,password):
    print("Login function called")
    if username in UTENTI and UTENTI[username] == password:
        print("LOGGATO")
        return True
    else:
        print("NON LOGGATO")
        return False

def signin(username,password):
    if username in UTENTI:
        print("UTENTE ESISTENTE")
        return False
    else:
        print("UTENTE REGISTRATO")
        UTENTI[username] = password
        return True