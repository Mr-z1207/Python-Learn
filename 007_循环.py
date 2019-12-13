L = [1, 2, 3, 4, 5]
Sum = 0
# for...in...循环
for i in L:
    Sum = Sum + i
    print(Sum)

L = [1, 2, '3', 4, 5]
Sum = 0
# for...in...循环
for i in L:
    # 不支持+的操作数类型：“int”和“str”
    # int() 把str 转换成int
    Sum = Sum + int(i)
    print(Sum)

# Python提供一个range()函数，可以生成一个整数序列
R = range(1, 1001)
# 再通过list()函数可以转换为list
Lr = list(R)

Sum = 0
for i in Lr:
    Sum += i
print(Sum)

# while循环
List = [12, 33, 25, 87, 22, 14, 49, 71]
# 奇偶分开
ou = []
ji = []
while len(List) > 0:
    item = List.pop()
    if item % 2 == 0:
        ou.append(item)
    else:
        ji.append(item)
print(ou, ji)

# break语句可以在循环过程中直接退出循环，
# 而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
