from functools import reduce
# map()函数接收两个参数，一个是函数，一个是Iterable
# 返回一个Iterator
L = [1, 2, 3, 4, 5]


def fn1(x):
    x = x ** 2
    return x


L = list(map(fn1, L))
print(L)
# map()作为高阶函数，它把运算规则抽象了可以计算任意复杂的函数
L = list(map(str, L))
print(L)


# #### reduce ####
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    result = x + y
    return result


RES = reduce(add, [1, 2, 3, 4])
print(RES)


# #######  test  ##########
L = ['adam', 'LISA', 'barT']


def Slower(x):
    return x[0].upper() + x[1:].lower()


newL = map(Slower, L)
print(list(newL))

# #######  test  ##########
L = [3, 5, 7, 9]


def prod(x, y):
    return x * y


RES = reduce(prod, L)
print(RES)
