import socket
import traceback

HOST = ''                 # Комп'ютер для з'єднання
PORT = 15555              # Порт для з'єднання

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

s.bind((HOST, PORT))        # зв'язати з комп'ютером та портом
s.listen(5)                 # очікувати на з'єднання

storage = {} # ключ -- для кого, значення -- [(від кого, повідомлення), ...]

try:
    while True:
        print('Before accept() is called')
        conn, addr = s.accept()     # отримати параметри з'єднання
        print('After accept() is called', conn, addr)
        print('Connected by', addr)

        data = conn.recv(1024)  # отримати дані (рядок байтів)
        ds = data.decode()
        userdata = ds.split(',')
        if len(userdata) < 3:
            conn.close()
            continue

        senderid = userdata[0]
        towhom = userdata[1]
        msg = ','.join(userdata[2:])
        print('>> from:', senderid)
        print('>> to:', towhom)
        print('>> message:', msg)

        resp = 'ok'
        conn.sendall( resp.encode() )
        conn.close()  # закрити з'єднання
except KeyboardInterrupt:
    print('Дочасне завершення програми через Ctrl+C або його аналог')
except:
    print('Помилка')
    traceback.print_exc()

s.close()
print('Сервер завершив свою роботу!')
