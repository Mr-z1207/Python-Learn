# 把函数作为参数传入，这样的函数称为高阶函数
# 变量可以指向函数
print(abs(-10))
print(abs)

f = abs
print(f(-10))
print(f)
# 函数名其实就是指向函数的变量！


# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，
def fn(a, b, f):
    result = f(a) + f(b)
    print(result)


fn(-10, 5, abs)
