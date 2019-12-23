a = ord('A')
b = ord('中')
c = chr(65)
d = chr(20013)
print(a, b, c, d)
print('\u4e2d \u6587')
e = b'abc'
print('bytes类型', e)
f = len('ABC')
print('ABC 字符串长度', f)

# 在字符串内部，%s表示用字符串替换，
# %d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，
# 顺序要对应好。如果只有一个%?，括号可以省略
# 其中，格式化整数和浮点数还可以指定是否补0和整数%02d与小数%.2f的位数：
print('您好，%s(先生/女士):您%02d月话费余额为%.2f元' % ('文嵩', 5, 28.96))
# 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('GDP增长%s%%' % (6.27))

# encode()方法可以编码为指定的bytes
a = 'ABC'.encode('ascii')
print(a)
a = '中文!'.encode('utf-8')
print(a)
# 要把bytes变为str，就需要用decode()方法
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
b = a.decode('utf-8', errors='ignore')
print(b)
