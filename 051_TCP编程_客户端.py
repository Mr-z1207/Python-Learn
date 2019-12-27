# 我们要创建一个基于TCP连接的Socket
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务，指定主机和端口
s.connect(('www.baidu.com', 80))

# 发送数据：
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# 接收数据:
# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，
# 因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
data = b''.join(buffer)

# 关闭连接:
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，
header, html = data.split(b'\r\n\r\n', 1)
# 把HTTP头打印出来，
print(header.decode('utf-8'))
# 网页内容保存到文件：
with open('file/051-file/baidu.html', 'wb') as f:
    f.write(html)
