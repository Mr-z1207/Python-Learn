# 如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fn(x):
    if x == 1:
        return 1
    return x * fn(x-1)


res = fn(5)
print(res)
