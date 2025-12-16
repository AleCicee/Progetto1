import http.server
import socketserver
import login as logFile

PORTA = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
   def do_POST(self):
      if self.path == "/login":
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
            
        # PARTE 1: CAPIRE COME FUNZIONA LO SPLIT
        # Il browser invia: "u=Mario&p=1234"
        parts = body.split('&')             # Diventa lista: ['u=Mario', 'p=1234']
        parte_nome = parts[0]               # Prendiamo il primo pezzo: 'u=Mario'
        dati_nome = parte_nome.split('=')   # Spacchiamo sull'uguale: ['u', 'Mario']
        username = dati_nome[1]             # Prendiamo il valore: 'Mario'
        password = parts[1].split("=")[1]
        
        check = logFile.login(username,password)
        
        if check == False: #NON LOGGATO
            f = open('registration.html', "r")
            codice_html = f.read()
            f.close()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(codice_html.encode('utf-8')) 
            
        if self.path == "/register":
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length).decode('utf-8')
                
            # PARTE 1: CAPIRE COME FUNZIONA LO SPLIT
            # Il browser invia: "u=Mario&p=1234"
            parts = body.split('&')             # Diventa lista: ['u=Mario', 'p=1234']
            parte_nome = parts[0]               # Prendiamo il primo pezzo: 'u=Mario'
            dati_nome = parte_nome.split('=')   # Spacchiamo sull'uguale: ['u', 'Mario']
            username = dati_nome[1]             # Prendiamo il valore: 'Mario'
            password = parts[1].split("=")[1]
            
            check = logFile.signin(username,password)
            
            if check: #se si è registrato
                f = open('login.html', "r")
                codice_html = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(codice_html.encode('utf-8'))
                

with socketserver.ThreadingTCPServer(("",PORTA),Handler) as httpd:
    print("Server on")
    httpd.serve_forever()