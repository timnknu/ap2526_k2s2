import socketserver
import traceback

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання



class MyClientHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(self.client_address)
        print('-------')
        all_received_data = b''
        while True:
            data = self.rfile.read(88)
            all_received_data = all_received_data + data
            print('data from client socket:', data)
            if len(data)==0:
                print('recv returned empty array')
                break
        print('LOOP FINISHED')
        print('ALL DATA IS', all_received_data)

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
