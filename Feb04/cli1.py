import socket

HOST = 'localhost'    # Комп'ютер для з'єднання з сервером
PORT = 15555          # Порт для з'єднання з сервером

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # з'єднатися з сервером


to_send = "This is a test string"
barr = to_send.encode()
print(barr, type(barr))
s.sendall(barr)

data = s.recv(1024)     # отримати відповідь сервера
ds = data.decode()
print(ds)

s.close()                   # завершити з'єднання