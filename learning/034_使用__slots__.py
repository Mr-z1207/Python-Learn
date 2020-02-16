from types import MethodType


class Student(object):
    pass


# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
s = Student()
s.name = 'Tom'


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
def sayAge(self, age):
    print('%s,' % self.name, age)


# 如果我们在模块中定义一个方法，而不是在类中定义一个方法，
# 那么此时这个方法并不是对象的实例方法，
# 但是我们可以将这个放法作为属性赋值给对象的 某一个属性。
s.sayAge = sayAge
# 但是在调用的时候person对象不会作为self参数传递到run方法内部。
# 原因是run属性对应的方法并不是person对象的属性
# s.sayAge(18) 报错
# 实例方法在调用的时候自动传入被调用对象作为self参数，
# 那么可以使用typesMethodType(methodName,instance) 方法实现
# 其中第一个参数为一个方法名称， 第二个参数是一个实例对象
s.sayAge = MethodType(sayAge, s)
s.sayAge(18)

# 为了给所有实例都绑定方法，可以给class绑定属性/方法
Student.pot = 3
Student.sayAge = sayAge
p = Student()
print(p.pot)
print(s.pot)
p.name = 'Any'
p.sayAge(20)


# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Person(object):
    __slots__ = ('name', 'age')


p1 = Person()
p1.name = 'Tom'
p1.age = 18
# 由于'x'没有被放到__slots__中，所以不能绑定x属性
# p1.x = 3 报错

print(p1.name)
print(p1.age)

# 定义在类上是可以的
Person.x = 3
print(p1.x)
