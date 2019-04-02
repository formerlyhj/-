import socket

# 初始化socket，设置IP地址和端口号
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 43999)
server.bind(address)

# 服务器端侦听和等待连接
server.listen(5)
conn, addr = server.accept()

# 接收图片
print('接受---->')
img = open('images/new_picture.jpg', 'wb')

while True:
    img_data = conn.recv(1024)
    if not img_data:
        break

    img.write(img_data)

server.close()
print('读档完毕')


