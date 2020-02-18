# 要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()
G = (i for i in range(0, 5))
print(G)
# 可以通过next()函数获得generator的下一个返回值
print('next:::', next(G))
print('next:::', next(G))
# print('next', next(G))
# print('next', next(G))
# print('next', next(G))

# generator保存的是算法，每次调用next(g)，
# 就计算出g的下一个元素的值，直到计算到最后一个元素
# 没有更多的元素时，抛出StopIteration的错误。

# 还可以使用for循环，因为generator也是可迭代对象
# next()之后就打印不出来了,从next之后的开始循环
for i in G:
    print('for:::', i)


# 如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator
def fn():
    print('sp1')
    yield(1)
    print('sp2')
    yield(2)
    print('sp3')
    yield(3)
    print('sp4')
    yield(4)
    print('sp5')
    return(5)


Gfn = fn()
next(Gfn)
next(Gfn)
next(Gfn)
next(Gfn)
next(Gfn)

# for i in Gfn:
#     print('for:::', i)
