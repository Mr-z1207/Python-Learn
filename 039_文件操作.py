# 操作文件和目录
# Python内置的os模块也可以直接调用操作系统提供的接口函数
import os

# 操作系统类型,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
# print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')
# key = os.environ.get('PATH')
# print(key)


# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 查看当前目录的绝对路径:
os.path.abspath('.')

# 创建一个目录:
# os.mkdir('./file/039-file/test')
# 删掉一个目录:
# os.rmdir('./file/039-file/test')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
path = os.path.join('./file/039-file', 'test')
print(path)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# os.path.splitext()可以直接让你得到文件扩展名

# 重命名假定目录下有一个test.txt文件
# os.rename('file/039-file/test.txt', 'file/039-file/test/test.txt')
# 删掉文件
# os.remove('test.py')
