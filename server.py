import http.server
import socketserver
import login as logFile
import play
import json

PORTA = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/login":
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length).decode('utf-8')
            parts = body.split('&')
            username = parts[0].split('=')[1]
            password = parts[1].split('=')[1]
            check = logFile.login(username, password)
            if check == False:  # NON LOGGATO
                f = open('registration.html', "r")
                codice_html = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(codice_html.encode('utf-8')) 
            else:
                f = open('game.html', "r")
                codice_html = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(codice_html.encode('utf-8'))
                
        elif self.path == "/register":
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length).decode('utf-8')
            parts = body.split('&')
            username = parts[0].split('=')[1]
            password = parts[1].split('=')[1]
            check = logFile.signin(username, password)
            print(check)
            if check:  # se si è registrato
                f = open('index.html', "r")
                codice_html = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(codice_html.encode('utf-8'))
            else:
                f = open('registration.html', "r")
                codice_html = f.read()
                f.close()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(codice_html.encode('utf-8'))
                
        elif "id=" in self.path:
            id = int(self.path.split("=")[1])  # mossa player

            cpu_move = play.make_move(id)
            check_win = play.check_win()

            response = {
                "cpu_move": cpu_move,   # può essere ""
                "winner": None          # "CPU", "PLAYER", None
            }

            if check_win == "0":
                response["winner"] = "CPU"
            elif check_win == "1":
                response["winner"] = "PLAYER"

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))

            play.printBoard()
        # =======================
        # RESET TRIS
        # =======================
        elif self.path == "/reset_tris":
            play.reset()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))


with socketserver.ThreadingTCPServer(("", PORTA), Handler) as httpd:
    print("Server on")
    httpd.serve_forever()
                

with socketserver.ThreadingTCPServer(("", PORTA), Handler) as httpd:
    print("Server on")
    httpd.serve_forever()