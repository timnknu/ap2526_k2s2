import socket
import time

HOST = 'localhost'    # Комп'ютер для з'єднання з сервером
PORT = 15555          # Порт для з'єднання з сервером

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # з'єднатися з сервером

print('Connection established')
time.sleep(3)

print('sending data...')
txt = 'MESSAGE!MESSAGE!MESSAGE!MESSAGE!MESSAGE!MESSAGE!MESSAGE!MESSAGE!'
s.sendall( txt.encode() )
time.sleep(3)
txt = '222222222222222222222222'
s.sendall( txt.encode() )


time.sleep(10)
print('Exiting...')

s.close()                   # завершити з'єднання