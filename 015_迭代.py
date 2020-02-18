# 我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代
# 在Python中，迭代是通过for ... in来完成的
# java 是通过for(var i = 0; i < arr.length; i++)
# 在Python中，迭代可以用在list、tuple、str、int、dict
L = ['aa', 'bb', 'cc', 'dd']
for i in L:
    print(i)

# 默认情况下，dict迭代的是key。
dic = {'name': 'Tom', 'age': 18, 'city': 'BeiJing'}
for i in dic:
    print(i)
# 如果要迭代value，可以用for value in d.values()
for i in dic.values():
    print(i)
# 如果要同时迭代key和value，可以用for k, v in d.items()
for i in dic.items():
    print(i)
for k, v in dic.items():
    print(k, v)


# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对
for k, v in enumerate(L):
    print(k, v)
