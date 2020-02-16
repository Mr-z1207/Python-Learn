# 实例属性和类属性


# 给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    # 如果Student类本身需要绑定一个属性呢？
    # 可以直接在class中定义属性，这种属性是类属性，归Student类所有
    grade = '3'

    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90
# 因为实例并没有name属性，所以会继续查找class的name属性
print(s.grade)
# 打印Student类的name属性
print(Student.grade)
# 给实例绑定grade属性
s.grade = '4'
# 因为实例有name属性，不会继续查找class的name属性
print(s.grade)
# 但是类属性并未消失，用Student.name仍然可以访问
print(Student.grade)
# 删除实例的name属性
del s.grade
