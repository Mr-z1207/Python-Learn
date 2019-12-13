# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
class Student(object):
    # 定义基本属性
    i = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
    # 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
    # 构造方法
    def prt(self):
        print(self)
        print(self.__class__)
        # 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
        print('%s : %s' % (self.name, self.score))


t = Student('one', 'tow')
t.prt()
