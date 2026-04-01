import http.server
import traceback
import urllib

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання


class MyClientHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('Process GET', self.path)

        s = urllib.parse.urlsplit(self.path)
        r = urllib.parse.parse_qs(s.query)

        if s.path == "/":
            # показати основну сторінку
            with open('page273.html') as f:
                txt = f.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(txt.encode())

        elif s.path == "/processdata":
            # обробити дані форми і сформувати сторінку з результатом обробки
            selected_numbers_list = r.get('q1', [])
            if len(selected_numbers_list) == 0:
                self.send_response(200)
                self.end_headers()
                self.wfile.write("""<!DOCTYPE html><html><head><meta charset="utf-8"></head>
<body><h1>А чи точно не треба було обрати жоднго варіанту?</h1></body></html>
                """.encode())
            else:
                res = sum([int(x) for x in selected_numbers_list])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"<h1>Результат обробки:{res}</h1>".encode())
        else:
            self.send_response(200)
            #self.headers.add_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("ERROR: wrong address кирилиця".encode())


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
