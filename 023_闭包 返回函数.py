# 返回函数 函数作为返回值
# ####  test  ####


def fn():
    n = 0

    def cont():
        nonlocal n
        n = n + 1
        print(n)
    return cont


f = fn()
f()
f()
f()
f()
f()

# global关键字修饰变量后标识该变量是全局变量，
# 对该变量进行修改就是修改全局变量，
# 而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，
# 如果上一级函数中不存在该局部变量，nonlocal位置会发生错误
