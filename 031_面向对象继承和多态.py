# 有一个Person类，每个人都有名字和年龄
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print('My name is %s' % self.name)

    def say_info(self):
        print('''姓名：%s
年龄：%s''' % (self.name, self.age))


p1 = Person('Tom', 28)
p1.say_name()
p1.say_info()


# 有一个学生类，学生也是个人，而且还有特有的分数
# 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，
# 而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，
# 从左到右查找基类中是否包含方法。
class Student(Person):
    def __init__(self, name, age, score):
        # 调用父类的构函
        Person.__init__(self, name, age)
        self.score = score

    # 覆写父类的方法
    def say_info(self):
        print('''姓名：%s
年龄：%s
成绩：%s''' % (self.name, self.age, self.score))

    def say_grade(self):
        if 0 < self.score < 60:
            print('不及格')
        elif 60 < self.score < 70:
            print('D')
        elif 70 < self.score < 80:
            print('C')
        elif 80 < self.score < 90:
            print('B')
        elif 90 < self.score < 100:
            print('A')


s1 = Student('Bob', 18, 95)
# 从父类继承过来的方法
s1.say_name()
# 覆写父类的方法
s1.say_info()
# 自己的方法
s1.say_grade()

# p1是person类型，而S1， 既是person类型，又是student类型，这就是多态
