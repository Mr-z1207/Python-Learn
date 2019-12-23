# contextlib
from contextlib import contextmanager
# Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭
# 见038_文件读写.py


# 并不是只有open()函数返回的fp对象才能使用with语句。
# 实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        print(exc_value)
        print(traceback)
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


# 紧跟with后面的语句被求值后，"返回对象"的__enter__()方法被调用，
# 这个方法的返回值将被赋值给as后面的变量。
# 当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
with Query('Bob') as q:
    q.query()


# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下
class Query:
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

    @contextmanager
    def create_query(name):
        print('Begin')
        q = Query(name)
        yield q
        print('End')


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name, age):
    print("<%s>" % name)
    yield age
    print("</%s>" % name)


with tag("h1", 11) as i:
    print("hello")
    print(i)
    print("world")
