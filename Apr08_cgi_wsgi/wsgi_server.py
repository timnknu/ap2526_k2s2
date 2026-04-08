import wsgiref.simple_server
import traceback


HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання


def f(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html')]  # HTTP Headers
    start_response(status, headers)

    txt = "<html><body><h1>hello</h1></body></html>"
    return [txt.encode()]

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
