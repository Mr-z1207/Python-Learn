# Python内建的filter()函数用于过滤序列。
# 把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素
L = list(range(10))
print(L)


# 删掉奇数，只保留偶数
def fn1(x):
    return x % 2 == 0


newL = filter(fn1, L)
print(list(newL))

# 把一个序列中的空字符串删掉
L = ['A', '', 'B', None, 'C', '      ']


def fn2(x):
    # Python strip() 方法用于移除字符串头尾指定的字符或字符序列
    return x and x.strip()


newL = filter(fn2, L)
print(list(newL))


# 用filter求素数
def _old_list():
    n = 1
    while True:
        n = n + 1
        yield n


def fn3(n):
    # lambda相当于匿名函数，lambda 参数: 返回值函数体
    return lambda x: x % n > 0


def _new_list():
    it = _old_list()
    while True:
        n = next(it)
        yield n
        it = filter(fn3(n), it)


nl = _new_list()

for n in nl:
    if n < 1000:
        print(n)
    else:
        break


# ###### test: 筛选出回数 ########
L = list(range(500))


def is_palindrome(x):
    x = str(x)
    return x == x[::-1]


isp = filter(is_palindrome, L)
print(list(isp))
