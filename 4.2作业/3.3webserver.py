import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('10.2.2.201', 8080)
server.bind(server_address)
server.listen(1)
print('服务器已启动！')
while True:
    client_connection, client_address = server.accept()
    request = client_connection.recv(1024)
    print(request)
    http_response = b"HTTP/1.1 200 OK\r\n\r\n" \
                    b"hello,world!"
    client_connection.send(http_response)
    client_connection.close()
