import socketserver
import traceback

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання


class MyClientHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(self.client_address)
        print('-------')
        all_received_data = b''
        # PUT <filename> 12345000\n
        # <bytes of data -- 1234500>
        header = self.rfile.readline()
        hs = header.decode()
        print(hs, type(hs))
        cmd, fnm, len_as_str = hs.split()
        L = int(len_as_str)
        print('we are about to receive', L)

        with open(fnm, 'wb') as fo:
            data = self.rfile.read(L)
            if len(data) == L:
                print('Data received')
                fo.write(data)
            else:
                print(len(data))
                print('Помилка: Ми отримати не ту кількість байтів, яку очікували!')
        print('LOOP FINISHED')

        ######


####################

srv = socketserver.TCPServer((HOST, PORT), MyClientHandler, bind_and_activate=False)
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
