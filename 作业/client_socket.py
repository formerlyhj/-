import socket

# 初始化socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器端
address = ('127.0.0.1', 43999)
client.connect(address)


# 发送图片
print('传输--->')
img = open('images/picture.jpg', 'rb')  # 打开本地一张图片

while True:
    img_data = img.readline(1024)

    if not img_data:
        break

    client.send(img_data)

client.close()
print('完成！')
