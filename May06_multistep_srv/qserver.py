import http.server
import traceback
import urllib
import re

from pyasn1_modules.rfc4985 import srvName

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання

import queue
import threading

user_to_srv = queue.Queue()
srv_to_user = queue.Queue()

# URL: http://domain/<user-id>/script?param=value&...

def thread_func():
    def web_input(body_str, resp_code = 200, headers_list = []):  # prompt: ()
        srv_to_user.put(
            (resp_code, headers_list, body_str.encode())
        )
        return user_to_srv.get()
    #
    print('>>user session started')
    # сесія взаємодії з користувачем
    with open('quest1.html') as f:
        txt = f.read()
    res = web_input(txt)
    print(res)
    print('>>first web_input finished')

    with open('res1.html') as f:
        txt = f.read()
        txt = txt.replace('###ABC###', str(res))
    res = web_input(txt)
    print(res)
    print('>>second web_input finished')



threading.Thread(target=thread_func, daemon=True).start()

class MyClientHandler(http.server.SimpleHTTPRequestHandler):
    def _communicate(self, data_for_func):
        path = data_for_func[1]
        if re.match(r'/\d+/script', path):
            user_to_srv.put(data_for_func)

            res = srv_to_user.get()  # (resp_code, [headers], body_bytes)
            resp_code, headers_list, body_bytes = res

            self.send_response(resp_code)
            for h in headers_list:
                self.send_header(h[0], h[1])
            self.end_headers()
            self.wfile.write(body_bytes)
        else:
            if data_for_func[0] == 'GET':
                super().do_GET()
            elif data_for_func[0] == 'POST':
                super().do_POST()
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Wrong headers".encode())

    def do_GET(self):
        print('Process GET', self.path)
        # if self.path == '/':
        #     with open('index.html') as f:
        #         txt = f.read()

        self._communicate( ('GET', self.path, {}) )

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
