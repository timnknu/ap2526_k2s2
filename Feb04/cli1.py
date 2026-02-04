import socket
import traceback

HOST = 'localhost'    # Комп'ютер для з'єднання з сервером
PORT = 15555          # Порт для з'єднання з сервером

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # з'єднатися з сервером
try:
    userid = input("Enter you nickname:")
    assert userid.find(',') == -1
    towhom = input("To whom you would like to send a message?")
    if len(towhom) == 0:
        # якщо нікому не відправляємо, значить хочемо отримати повідомлення, накопичені на сервері для нас
        msg = ''
        data_to_send = f'{userid},{towhom},{msg}'
        s.sendall( data_to_send.encode() )
        data = s.recv(1024)     # отримати відповідь сервера
        ds = data.decode()
        print(ds)
    else:
        assert towhom.find(',') == -1
        msg = input("Now enter your message")

        data_to_send = f'{userid},{towhom},{msg}'
        print('[debug] sending to server:', data_to_send)

        s.sendall( data_to_send.encode() )

        data = s.recv(1024)     # отримати відповідь сервера
        ds = data.decode()
        print(ds)
except:
    print('Помилка')
    traceback.print_exc()

s.close()                   # завершити з'єднання