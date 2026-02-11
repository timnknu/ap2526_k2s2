import socketserver
import traceback

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання



class MyClientHandler(socketserver.StreamRequestHandler):
    def handle(self):
        client_socker = self.request
        print('Request from client', client_socker)
        print(self.client_address)
        print('-------')
        all_received_data = b''
        print(type(self.rfile), type(self.wfile))
        while True:
            data = client_socker.recv(1024)
            all_received_data = all_received_data + data
            if len(all_received_data) == 150:
                break
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
