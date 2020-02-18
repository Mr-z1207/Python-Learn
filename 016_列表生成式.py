# 列表生成式即List Comprehensions可以用来创建list的生成式
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list(range(1, 11))
print(L)
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
# 可以用循环，但是太繁琐
L = []
for i in list(range(1, 11)):
    L.append(i * i)
print(L)
# 列表生成式则可以用一行语句代替循环生成上面的list
L = [i * i for i in range(1, 11)]
print(L)

# for循环后面还可以加上if判断
L = [i * i for i in range(1, 11) if i % 2 == 0]
print(L)

# 还可以使用两层循环
L = [i + k for i in 'ABCD' for k in 'XY']
print(L)

# 其他的
L = [(k, v) for k, v in enumerate(['aa', 'bb', 'cc'])]
print(L)

L = ['Hello', 'World', 18, 'IBM', 'Apple']
L = [s.lower() for s in L if isinstance(s, str)]
print(L)
