# Python内置的sorted()函数就可以对list进行排序：
L = sorted([36, 5, -12, 9, -21])
print(L)

# 接收一个key函数来实现自定义的排序
L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)

# 对字符串来说,按照ASCII的大小比较的，'Z' < 'a'
L = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(L)

# 我们给sorted传入key函数，即可实现忽略大小写的排序
L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(L)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(L)

# #### test ####
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 按名字排序
def fn1(x):
    return x[0].lower()


L = sorted(L, key=fn1)
print(L)


# 按成绩从高到低排序
def fn2(x):
    return (x[1], x[0])


L = sorted(L, key=fn2)
print(L)

# sorted(iterable, cmp=None, key=None, reverse=False)
# 参数说明：

# iterable -- 可迭代对象。
# cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
