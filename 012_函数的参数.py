# 普通参数
def fn1(x):
    print(x)


fn1(1)


# 默认参数
def fn2(x=2):
    print(x)


fn2()


# 定义默认参数要牢记一点：默认参数必须指向 ####不变对象####！
def fn3(x=[]):
    x.append('end')
    print(x)


fn3()
# 函数似乎每次都“记住了”上次添加了'END'后的list
fn3()


# 可变参数  在参数前面加了一个*号(相当于js的扩展参数 ...[])
# 参数numbers接收到的是一个tuple
def fn4(*numbers):
    result = 0
    for i in numbers:
        result = result + i
    print(result)


# 调用该函数时，可以传入任意个参数，包括0个参数
fn4()
fn4(1, 2, 3)
# 如果已经有一个list或者tuple，要调用一个可变参数
List = [1, 2, 3]
fn4(*List)


# 关键字参数 在参数前面加**号( **kw )
def fn5(name, age, **kw):
    print('name=', name)
    print('age=', age)
    print('**kw=', kw)


fn5('Tom', 18)
# 函数person除了必选参数name和age外，还接受关键字参数kw
fn5('Tom', 18, city='Bj')
# 可以传入任意个数的关键字参数
fn5('Tom', 18, city='Bj', phone='13298448865')
# 可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
dic = {'city': 'Bj', 'phone': '13298448865'}
fn5('Tom', 18, **dic)


# 命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def fn6(name, age, *, city, job):
    print(name, age, city, job)


# 关键字只能说city、job且不能省略
fn6('Tom', 18, city='Bj', job='Student')


# 如果函数定义中有一个可变参数，后面的命名关键字参数就不需要特殊分隔符
def fn7(name, age, *args, city, job):
    print(name, age, args, city, job)


fn7('Tom', 18, *[1, 2, 3], city='Bj', job='Student')


# 参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
