# 以map()函数为例，计算f(x)=x2时，
# 除了定义一个f(x)的函数外，还可以直接传入匿名函数(
M = map(lambda x: x ** 3, range(10))
print(list(M))

# 匿名函数有个限制，就是只能有一个表达式，
# 不用写return，返回值就是该表达式的结果。

# ####  test  ####
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
