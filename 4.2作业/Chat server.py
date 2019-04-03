import socket
from threading import Thread

conn_list = list()


def conn_recv(conn, conn_addr):
    while 1:
        msg = conn.recv(65535)
        msg = msg.decode()
        print('收到来自{}的消息{}'.format(conn_addr, msg))
        return_msg = '收到来自{}的消息{}'.format(conn_addr, msg)
        # 加上encode，将普通字符串转换成二进制
        for conn in conn_list:
            conn.send(return_msg.encode())
# socket里面第一个写使用哪一个网络协议，第二个写使用哪个运输成协议


def conn_server(conn_addr):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP和端口
    server.bind(conn_addr)
    print('服务器已开启！')
    server.listen(10)

    while 1:
        try:
            conn, conn_addr = server.accept()
            conn_list.append(conn)
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