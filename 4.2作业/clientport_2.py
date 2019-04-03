import socket
from threading import Thread
clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# addr = ('127.0.0.1', 61212)
clien.connect(('127.0.0.1', 61212))


def conn_send(clien):
    while 1:
        msg = input('输入消息：')
        try:
            clien.send(msg.encode())
        except Exception:
            break


def conn_recv(clien):
    while 1:
        return_msg = clien.recv(65535)
        if not return_msg:
            break
        print(return_msg.decode())


t1 = Thread(target=conn_send, args=(clien,))
t2 = Thread(target=conn_recv, args=(clien,))

t1.start()
t2.start()
print('启动')
t1.join()
t2.join()
print('结束')
