# collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


# ########  namedtuple  ########
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
# >>> p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
# 用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(2, 6)
print(p1.x)

# 可以验证创建的Point对象是tuple的一种子类
print(isinstance(p1, Point))
print(isinstance(p1, tuple))


# ########  deque  ########
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])

q.append('x')
q.appendleft('y')
print(q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
q.popleft()
print(q)

# ########  defaultdict  ########
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
d = defaultdict(lambda: 'N/A', {'key1': 1, 'key2': 2})
print(d['key1'])
print(d['key2'])
print(d['key3'])

# ########  OrderedDict  ########
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
# *****************************************************************


# ########  ChainMap  ########
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# 应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
# 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数

# 下面的代码演示了如何查找user和color这两个参数：

# from collections import ChainMap
# import os, argparse

# # 构造缺省参数:
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }

# # 构造命令行参数:
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = { k: v for k, v in vars(namespace).items() if v }

# # 组合成ChainMap:
# combined = ChainMap(command_line_args, os.environ, defaults)

# # 打印参数:
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])
# 没有任何参数时，打印出默认参数：

# $ python3 use_chainmap.py
# color=red
# user=guest
# 当传入命令行参数时，优先使用命令行参数：

# $ python3 use_chainmap.py -u bob
# color=red
# user=bob
# 同时传入命令行参数和环境变量，命令行参数的优先级较高：

# $ user=admin color=green python3 use_chainmap.py -u bob
# color=green
# user=bob

# ########  Counter  ########
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for i in 'programming':
    c[i] = c[i] + 1

print(c)
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
