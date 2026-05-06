import http.server
import traceback
import urllib


HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання

import queue
import threading

user_to_func = queue.Queue()
func_to_user = queue.Queue()

def thread_func():
    while True:
        req = user_to_func.get()
        #####....обробка....
        txt = 'Request was: '+ str(req)
        func_to_user.put(
            (
                200, # resp_code
                [],
                txt.encode()
            )
        )

threading.Thread(target=thread_func, daemon=True).start()

class MyClientHandler(http.server.SimpleHTTPRequestHandler):
    def _communicate(self, data_for_func):
        user_to_func.put(data_for_func)

        res = func_to_user.get()  # (resp_code, [headers], body_bytes)
        resp_code, headers_list, body_bytes = res

        self.send_response(resp_code)
        for h in headers_list:
            self.send_header(h[0], h[1])
        self.end_headers()
        self.wfile.write(body_bytes)

    def do_GET(self):
        print('Process GET', self.path)
        self._communicate( ('GET', self.path) )

    def do_POST(self):
        print('Process POST', self.path)
        cl = self.headers.get('Content-Length', '0')
        try:
            post_data = self.rfile.read(int(cl))
            params = post_data.decode()
            self._communicate(('POST', self.path, params))
        except:
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Wrong headers".encode())

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
