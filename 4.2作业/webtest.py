import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8080)
server.bind(server_address)
server.listen(1)
print('服务器已启动！')
while True:
    client_connection, client_address = server.accept()
    print('你有新的链接{}'.format(client_address))
    request = client_connection.recv(1024)
    print(request)
    http_response = b"HTTP/1.1 200 OK\r\n\r\n" \
                    b"hello,world!"
    client_connection.send(http_response)
    client_connection.close()
