# 在绑定属性时，如果我们直接把属性暴露出去，
# 虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩
# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 见 030_面向对象访问限制.py


# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student:
    # 把一个getter方法变成属性，只需要加上@property就可以了，
    @property
    def score(self):
        return self._score

    # property本身又创建了另一个装饰器@score.setter，
    # 负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        # 这里不能写score，会和方法名冲突
        self._score = value

    # 还可以定义只读属性，只定义getter方法，
    # 不定义setter方法就是一个只读属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    # 上面的birth是可读写属性，
    # 而age就是一个只读属性，因为age根据birth和当前时间计算出来


s1 = Student()
s1.score = 60
print(s1.score)

s1.birth = 2000
print(s1.age)
