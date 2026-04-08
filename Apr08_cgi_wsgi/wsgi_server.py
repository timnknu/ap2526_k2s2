import wsgiref.simple_server
import traceback
import urllib.parse
from os import environ

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання


def f(environ, start_response):
    status = '200 OK'  # HTTP Status
    pth = environ['PATH_INFO']
    if pth == "/":
        headers = [('Content-type', 'text/html')]  # HTTP Headers
        start_response(status, headers)
        with open('main_page_wsgi.html') as f:
            txt = f.read()

        return [txt.encode()]
    elif pth == "/processform":

        headers = [('Content-type', 'text/html')]  # HTTP Headers
        start_response(status, headers)
        qs = environ['QUERY_STRING']
        cl = environ.get('CONTENT_LENGTH', '')

        try:
            cl = int(cl)
        except:
            cl = 0

        post_data = environ['wsgi.input'].read(cl)
        post_data_dict = urllib.parse.parse_qs(post_data.decode())
        usertext = ''.join(post_data_dict.get('usertext', []))
        nwords = len(usertext.split())
        txt = f"""<html><body>number of words: {nwords}</body></html"""


        return [txt.encode()]
    else:
        headers = [('Content-type', 'text/plain')]  # HTTP Headers
        start_response(status, headers)
        return ["UNKNOWN REQUEST".encode()]


####################

srv = wsgiref.simple_server.WSGIServer((HOST, PORT), wsgiref.simple_server.WSGIRequestHandler, bind_and_activate=False)
srv.allow_reuse_port = True
srv.allow_reuse_address = True
srv.server_bind()
srv.server_activate()
srv.set_app(f)


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
