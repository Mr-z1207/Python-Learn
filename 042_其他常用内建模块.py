import base64
import itertools
# ####  base64  ####
# Base64是一种用64个字符来表示任意二进制数据的方法。
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')


# ####  itertools  ####
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# 首先，我们看看itertools提供的几个“无限”迭代器

# count()会创建一个无限的迭代器
natuals = itertools.count(1, 2)
for i in natuals:
    if i < 10:
        print(i)
    else:
        break

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABCDEFG')
i = 0
for s in cs:
    if i < 10:
        print(s)
        i = i + 1
    else:
        break

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
re = itertools.repeat('ABCDEFG', 3)
for i in re:
    print(i)


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1, 2)
ns = itertools.takewhile(lambda x: x < 10, natuals)
print(list(ns))


# itertools提供的几个迭代器操作函数更加有用
# ####  chain()  ####
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# ####  groupby()  ####
# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
