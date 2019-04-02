import socket

# 2个参数分别是： IPV4、TCP 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接，2个参数是： 网址、端口
s.connect(('www.baidu.com', 80))
# 向服务器发送请求,传递的参数是：1.请求方式 2.地址 3.链接方式（open or close）
# 注：‘GET / HTTP’这里的‘/’是跟目录的意思
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: close\r\n\r\n')

# 开始接受服务器传来的数据
buffer = []  # 新建一个空列表，buffer即缓存的意思
while True:
    d = s.recv(1024)  # 每次最多接收1k字节
    if d:  # 如果能正常接收到d
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭文件
s.close()

# 开始处理数据
# 分离网页头部与html
h, html = data.split(b'\r\n\r\n', 1)
# 以utf-8解码为正常文本
print(h.decode('utf-8'))
# 新建文件，将接收到的数据接入文件内
with open('baidu', 'wb')as f:
    f.write(h)

