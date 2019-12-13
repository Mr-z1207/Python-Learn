x = 21
# 根据Python的缩进规则，如果if语句判断是True，
# 就把缩进的两行print语句执行了，否则，什么也不做。
if x > 0:
    print('大于零')
# 也可以给if添加一个else语句
if x < 0:
    print('小于零')
else:
    print('>=0')
# 可以用elif做更细致的判断 elif else if 的缩写
if x > 100:
    print('大于100')
elif x > 50:
    print('大于100')
elif x > 20:
    print('大于20')
else:
    print('都不是')
# if判断条件还可以简写
# 只要x是非零数值、非空字符串、非空list等，就判断为True
if x:
    print('True')
