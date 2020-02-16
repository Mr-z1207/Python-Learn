import functools


# 由于函数也是一个对象，而且函数对象可以被赋值给变量
def sayHello():
    print('hello')


f = sayHello
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
print(f.__name__)

# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。


# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下
def log(func):
    # Python内置的functools.wraps 把原始函数的__name__等属性复制到wrapper()函数中
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 相当于运行 log(sayHi)
@log
def sayHi():
    print('Hi')


sayHi()
