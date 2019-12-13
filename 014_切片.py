L = list(range(50))
print(L)

# Python提供了切片（Slice）操作符
# 从索引10开始取，直到索引20为止，不包括20
print(L[10:20])

# 如果第一个索引是0，还可以省略
print(L[:5])

# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-5:-2])

# 每两个取一个
print(L[10:20:2])

# 倒这排序
print(L[30:20:-2])

# 甚至什么都不写，只写[:]就可以原样复制一个list
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
