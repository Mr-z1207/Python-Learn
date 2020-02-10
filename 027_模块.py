#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Weston Zhou'


# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
# 2行注释表示.py文件本身使用标准UTF-8编码；
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
import sys
# sys模块有一个argv变量，用list存储了""命令行""的所有参数。


def fn():
    argv = sys.argv
    if len(argv) == 1:
        print('hello %s' % (__author__))
    elif len(argv) == 2:
        print('Hello, %s!' % argv[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    fn()
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

# ####  命令行运行结果  ####
# C:\WEB\python_test>python 027_模块.py ZWS
# Hello, ZWS!


# （2）主程序所在目录是模块所在目录的父(或祖辈)目录
# 如下面程序结构:
# `-- src
#     |-- mod1.py
#     |-- mod2
#     |   `-- mod2.py
#     `-- test1.py
#     若在程序test1.py中导入模块mod2,
#     需要在mod2文件夹中建立空文件__init__.py文件
#     (也可以在该文件中自定义输出模块接口);
#      然后使用 from mod2.mod2 import * 或import mod2.mod2.
