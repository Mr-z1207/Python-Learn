# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储
# 差不多js里面的对象吧(json)
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print(d['Michael'])

# 存入键值对
d['Any'] = 88
print(d)

# 修改键值对
d['Bob'] = 70
print(d)

# 删除键值对
d.pop('Tracy')
print(d)

# 获取键值对
result = d.get('Anyyy')
print(result)
result = d.get('Anyyy', -1)
print(result)

# json.dumps	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象

# set和dict类似，也是一组key的集合，但不存储value。
# 要创建一个set，需要提供一个list作为输入集合
S = set([1, 2, 3])
# 它是无序的
print(S)
# 由于key不能重复，所以，在set中重复元素自动被过滤
S = set([1, 2, 2, 3, 3, 3, 4])
print(S)
# add(key)增加 remove(key)删除
# 可以重复添加，但不会有效果
S.add(5)
print(S)
S.add(4)
print(S)
S.remove(4)
print(S)
# 两个set可以做数学意义上的交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集 &
print(s1 & s2)
# 并集 |
print(s1 | s2)

ss = set([1, 2, (11, 22), 33])
print(ss)
