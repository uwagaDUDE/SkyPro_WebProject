
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = 'localhost'
port = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()
        self.wfile.write(bytes('Hello, World wide web!', 'utf-8'))

if __name__ == '__main__':
    server = HTTPServer((hostname, port), MyServer)
    print(f'Сервер запущен по адресу http://%s:%s' % (hostname, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print('Сервер выключен')