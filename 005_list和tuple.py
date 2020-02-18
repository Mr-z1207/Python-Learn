# list 列表（数组）
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmaster = ['Leo', 'Marry', 'Bob']
# 类似Js数组
print(classmaster)
# 数组长度
print(len(classmaster))
# 第一个元素
print(classmaster[0])
# 倒数第一个元素
print(classmaster[-1])
# 改变序号（下标）为0的元素
classmaster[0] = 'Any'
print(classmaster)
# 在末尾插入元素
classmaster.append('Tom')
print(classmaster)
# 在序号（下标）为2的地方插入元素
classmaster.insert(2, 'Jany')
print(classmaster)
# 删除末尾元素
classmaster.pop()
print(classmaster)
# 删除倒数第二个元素
classmaster.pop(-2)
print(classmaster)
# list里面的元素的数据类型也可以不同
List = [1, 'aaa', [True, 5.33e5], False]
print(List[2][1])

# tupie 另一种有序列表叫元组---元组
# tuple和list非常类似，但是tuple一旦初始化就不能修改
names = ('aaa', 'bbb', 'ccc')
print(names)
print(names[1])
# names[1] = 'ddd' 报错，无法更改
Tuple = ('aa', 'bb', [1, 2], 'cc')
print(Tuple)
Tuple[2][0] = 3
print(Tuple)
Tuple[2].append(66)
print(Tuple)
# 表面上看，tuple的元素确实变了，
# 但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，
# 指向永远不变。即指向'a'，就不能改成指向'b'，
# 指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

# 如果要定义一个空的tuple，可以写成()
L = ()
print(L)
# 但是，要定义一个只有1个元素的tuple
L = (1)
print(L)
# L = (1) 这是错的，这会把()看作是小括号，输出只能是数字1
L = (1,)
print(L)
# 需要这样写才行
