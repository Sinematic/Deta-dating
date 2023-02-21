import http.server
import socketserver
import os

class MonHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("appel de l'url :",self.path)
        if self.path == "/tapage.html":
            print("url dynamique")
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytearray("<html><body>","utf8"))
            self.wfile.write(bytearray("Ceci est ta page &agrave; toi","utf8"))
            self.wfile.write(bytearray("</body></html>","utf8"))
        elif self.path == "/secret":
            print("routage vers un fichier html")
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.copyfile(open(fichierHTML,'rb'),self.wfile)
        elif self.path == "/API":
            print("simulateur API")
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.copyfile(open(fichierAPI,'rb'),self.wfile)
        elif self.path == "/":
            print("protection du répertoire")
            self.send_response(404)
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)



fichierHTML = os.path.dirname(os.path.realpath(__file__))+"\mapage.html"
fichierAPI = os.path.dirname(os.path.realpath(__file__))+"\metros.json"

PORT = 8080
#Handler = http.server.SimpleHTTPRequestHandler            

# Astuce MonHandler est appelé en paramètre
with socketserver.TCPServer(("", PORT), MonHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
