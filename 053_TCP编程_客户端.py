# 我们要创建一个基于TCP连接的Socket
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务，指定主机和端口
s.connect(('127.0.0.1', 3000))

# 发送数据：
s.send(b'hello')

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

print(data.code('utf-8'))
