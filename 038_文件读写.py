# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
f = open('file/038-file/test.txt', 'r')
# 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
s = f.read()
print(s)
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open('file/038-file/test.txt', 'r') as file:
    data = file.read()
print(data)
# 详见Chrome收藏夹——杂七杂八

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
# 因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，
# 还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，
# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
f = open('file/038-file/gbk.txt', 'r', encoding='gbk', errors='ignore')
f.close()

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('file/038-file/gbk.txt', 'w') as file:
    file.write('你好')
with open('file/038-file/gbk.txt', 'r') as file:
    data = file.read()
print(data)
# 完整的语法格式为：
# open(file, mode='r', buffering=-1, encoding=None, errors=None,
# newline=None, closefd=True, opener=None)
# 参数说明:
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# 详见：https://www.runoob.com/python/file-methods.html
