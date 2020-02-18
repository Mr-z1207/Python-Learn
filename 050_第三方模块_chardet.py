# chardet
# 虽然Python提供了Unicode表示的str和bytes两种数据类型，
# 并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。

# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。
# 猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。

# 当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。
# chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。
import chardet

# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print(chardet.detect(b'Hello, world!'))
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
