import socketserver
import traceback

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання


class MyClientHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(self.client_address)
        print('-------')
        header_lines = []
        while True:
            line = self.rfile.readline()
            print('>>', line)
            s = line.decode(encoding='utf-8').rstrip()
            header_lines.append(s)
            if len(s) == 0:
                break
        #
        print('Початок запиту:')
        print(header_lines)

        ######


####################

srv = socketserver.ThreadingTCPServer((HOST, PORT), MyClientHandler, bind_and_activate=False)
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
