# 首先，我们来判断对象类型，使用type()函数：
print(type(123))
print(type('str'))
print(type(abs))

# type()不方便判断class类型
# 所以使用isinstance()
print(isinstance(123, int))


class Person:
    def __init__(self):
        self.lol = 101

    def __len__(self):
        return 10
    pass


class Student(Person):
    pass


class Computer_student(Student):
    pass


# 继承关系： Person > Student > Computer_student
P1 = Person()
S1 = Student()
C1 = Computer_student()
# C1 不仅是Computer_student类型， 也是Student Person 类型
print(isinstance(C1, Computer_student))
print(isinstance(C1, Student))
print(isinstance(C1, Person))
# C1 不仅是Student类型，也是 Person 类型 但不是Computer_student类型
print(isinstance(S1, Student))
print(isinstance(S1, Person))
print(isinstance(S1, Computer_student))

# isinstance还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple, int)))
print(isinstance((1,), (list, tuple, int)))
# (1) 这个相当于小括号，所以要向上面那样定义一个元素的tuple
print(isinstance((1), (list, tuple, int)))
print(isinstance('1', (list, tuple, int)))


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数,返回list
# L = dir('ABC')
# print(L)

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('ABC'))
print('ABC'.__len__())

# 我们自己写的类，如果也想用len(Person)的话，就自己写一个__len__()方法
print(len(P1))

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
L = dir(P1)
print(L)

print(hasattr(P1, 'lol'))
print(getattr(P1, 'lol'))
setattr(P1, 'lol', 202)
print(getattr(P1, 'lol'))
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(P1, 'ZoZ', 404))
