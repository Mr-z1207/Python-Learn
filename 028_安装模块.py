# 在Python中，安装第三方模块，是通过包管理工具pip完成的。

# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。

# 如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。

# 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。

# 注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。

# 例如，我们要安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
# 不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，
# 并且支持最新的Python 3。

# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，
# 必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
# pip install Pillow

# 安装常用模块
# 在使用Python时，我们经常需要用到很多第三方库，
# 例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。
# 用pip一个一个安装费时费力，还需要考虑兼容性。
# 我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，
# 它已经内置了许多非常有用的第三方库，我们装上Anaconda，
# 就相当于把数十个第三方模块自动安装好了，非常简单易用。

# 可以从Anaconda官网下载GUI安装包，安装包有500~600M，
# 所以需要耐心等待下载。网速慢的同学请移步国内镜像。下载后直接安装，
# Anaconda会把系统Path中的python指向自己自带的Python，
# 并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。