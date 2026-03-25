import http.server
import traceback

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання


class MyClientHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('Process GET', self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write("<h1>PAGE!!!</h1>".encode())


####################

srv = http.server.ThreadingHTTPServer((HOST, PORT), MyClientHandler, bind_and_activate=False)
srv.allow_reuse_port = True
srv.allow_reuse_address = True
srv.server_bind()
srv.server_activate()

print('Server is listening...')
try:
    srv.serve_forever()
except KeyboardInterrupt:
    print('Дочасне завершення програми через Ctrl+C або його аналог')
except:
    print('Помилка')
    traceback.print_exc()

srv.shutdown()

print('Сервер завершив свою роботу!')
