import http.server
import socketserver

PORTA = 8000

class Handler (http.server.SimpleHTTPRequestHandler):
   def do_POST(self):
      if self.path == "":
         


with socketserver.ThreadingTCPServer(("",PORTA),handler) as httpd:
   print("Server on")
   httpd.serve_forever()
   

