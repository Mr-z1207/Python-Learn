class Student:
    def __init__(self, name):
        self.name = name


s1 = Student('Any')

# 打印出一堆<__main__.Student object at ......>，不好看。
print(s1)


# 只需要定义好__str__()方法
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student is %s' % self.name

    __repr__ = __str__


s2 = Student('Bob')
print(s2)

# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看
# ### 控制台中 ###
# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。
# 但是通常__str__()和__repr__()代码都是一样的
# 见20行

# 实现一个__iter__()方法，类被用于for ... in循环
# Python的for循环就会不断调用
# 该迭代对象的__next__()方法拿到循环的下一个值
# def __iter__(self):
#       return self # 实例本身就是迭代对象，故返回自己

# 虽然能作用于for循环，看起来和list有点像，
# 但是，把它当成list来使用还是不行无法使用下标
# 需要实现__getitem__()方法


# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
class Student:
    def __init__(self, name):
        self.name = name


s = Student('Tom')
# print(s.score) 报错


# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
# 那就是写一个__getattr__()方法，动态返回一个属性。
class Student:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 38
        elif attr == 'age':
            return lambda: print(70)


s = Student('Tom')
# 当调用不存在的属性时，比如score，
# Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
print(s.score)
# 返回函数也是完全可以的
s.age()
# 任意调用如s.abc都会返回None,
# 这是因为我们定义的__getattr__默认返回就是None
print(s.abc)


# 利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain:
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


PATH = Chain().student.list
print(PATH)


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Test:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


t = Test('Jann')
t()

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(t))
