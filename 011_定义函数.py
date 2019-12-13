# 在Python中，定义一个函数要使用def语句
num = input('请输入一个数字：')


# 函数体前后需要两行空行
def funName(data):
    data = int(data)
    if data >= 0:
        return data
    else:
        return -data


result = funName(num)
print('绝对值：', result)


# 参数检查 内置函数isinstance()
def funName(data):
    if not isinstance(data, (int, float)):
        raise TypeError('bad operand type')
    if data >= 0:
        return data
    else:
        return -data


result = funName(num)
print('绝对值：', result)

# # lambda相当于匿名函数，lambda 参数: 返回值函数体(见:021_39行用法)
