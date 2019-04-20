import socket
from threading import Thread
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_list = list()


def conn_recv(conn, conn_addr):
    while 1:
        msg = conn.recv(65535)
        msg = msg.decode()
        if msg == 'exit':
            break
        return_msg = '收到来自{}的消息：{}'.format(conn_addr, msg)
        print(return_msg)
        for conn in conn_list:
            conn.send(return_msg.encode())
    conn.close()


def conn_server(conn_addr):
    server.bind(conn_addr)
    print('服务器已开启！')
    server.listen(10)
    lock = threading.Lock()
    while 1:
        try:
            conn, conn_addr = server.accept()
            lock.acquire()
            conn_list.append(conn)
            lock.release()
            print('加入链接{}'.format(conn_addr))
        except Exception:
            break
        t = Thread(target=conn_recv, args=(conn, conn_addr))
        t.start()

    server.close()
    print('服务器关闭！')


if __name__ == '__main__':
    server_addr = ('0.0.0.0', 61212)
    conn_server(server_addr)