# Python学习笔记

---

[TOC]

---

## 一、基本说明

本仓库为本人学习练习代码，仅供参考

## 二、常见问题

### 2.1 参数的顺序

参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

### 2.2 文件夹下面的自定模块如何引用

目录结构如下

    `-- src
        |-- mod1.py
        |-- mod2
        |   `-- mod2.py
        `-- test1.py

若在程序test1.py中导入模块mod2,需要在mod2文件夹中建立空文件__init__.py文件(也可以在该文件中自定义输出模块接口);然后使用 from mod2.mod2 import * 或import mod2.mod2

## 三、常用方法

### 3.1 字符串编码转换

> 参考 [004_字符串编码.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/004_%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%BC%96%E7%A0%81.py)

encode()方法可以编码为指定的bytes
要把bytes变为str，就需要用decode()方法

```python
a = 'ABC'.encode('utf-8')
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
b = a.decode('utf-8', errors='ignore')
```

### 3.2 list切片

> 参考 [014_切片.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/014_%E5%88%87%E7%89%87.py)

话不多说，，，看代码
```python
# Python提供了切片（Slice）操作符
# 从索引10开始取，直到索引20为止，不包括20
print(L[10:20])

# 如果第一个索引是0，还可以省略
print(L[:5])

# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-5:-2])

# 每两个取一个
print(L[10:20:2])
```

### 3.3 列表生成器

> 参考 [016_列表生成式.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/016_%E5%88%97%E8%A1%A8%E7%94%9F%E6%88%90%E5%BC%8F.py)

简单来说，一个列表 [ 被操作的item 一个循环 或者 一个判断 ]
```python
# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = [i * i for i in range(1, 11)]
```

### 3.4 格式化字符串

简省了字符串的拼接，更好的将变量加入到字符串当中

#### 3.4.1. printf 风格 `%`

```python
'我叫%s，今年%s岁，喜欢%s' %('小明','18','足球')
```
其中 `%s` 就是模板中的占位符，表示这个位置先占着，待会儿要有数据填入到这里。然后再提供一个元组`('小明','18','足球')`，里面依次存放需要填入到 `%s` 位置 的数据,还有补足位数，长度等方法，请自行探索

#### 3.4.2 f-string 格式化 `f''`

> 注意：这种写法必须要Python解释器是3.6 以后的版本才支持

f-string 格式化 就是在字符串模板前面加上f，然后占位符使用{} ,里面直接放入对应的数据对象。

```python
name = '小明'
age = '18'
like = '足球'

f'我叫{name}，今年{age}岁，喜欢{like}'
```

## 四、内建模块总结

### 4.1 datetime

> 参考 [040_常用内建模块-datatime.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/040_%E5%B8%B8%E7%94%A8%E5%86%85%E5%BB%BA%E6%A8%A1%E5%9D%97-datatime.py)

datetime是Python处理日期和时间的标准库。

### 4.2 collections

> 参考 [0041_常用内建模块-collections.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/041_%E5%B8%B8%E7%94%A8%E5%86%85%E5%BB%BA%E6%A8%A1%E5%9D%97-collections.py)

collections是Python内建的一个集合模块，提供了许多有用的集合类。

#### 4.2.1 namedtuple

如果我们想表示一个点 用 `x = (1, 2)` 很难看出来这是一个点的坐标.
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用

```python
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(2, 6)
print(p1.x)
```

#### 4.2.2 deque

使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。deque是为了高效实现插入和删除操作的双向列表.deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
```python
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

>>>
['y', 'a', 'b', 'c', 'x']
```

#### 4.2.3 defaultdict

使用dict时，如果引用的Key不存在，返回默认值

```python
d = defaultdict(lambda: 'N/A', {'key1': 1, 'key2': 2})
print(d['key1'])
print(d['key3'])

>>>
1
N/A
```

### 4.3 base64

> 参考 [042_其他常用内建模块.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/042_%E5%85%B6%E4%BB%96%E5%B8%B8%E7%94%A8%E5%86%85%E5%BB%BA%E6%A8%A1%E5%9D%97.py)

 Base64是一种用64个字符来表示任意二进制数据的方法。由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

 ### 4.4 itertools

 > 参考 [042_其他常用内建模块.py](https://github.com/Mr-z1207/Python-test/blob/master/learning/042_%E5%85%B6%E4%BB%96%E5%B8%B8%E7%94%A8%E5%86%85%E5%BB%BA%E6%A8%A1%E5%9D%97.py)

 Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。大概功能有

> - 创建一个无限的迭代器
> - 把传入的一个序列无限重复下去
> - 把一个元素无限重复下去
> - 可以把一组迭代对象串联起来，形成一个更大的迭代器
> - 把迭代器中相邻的重复元素挑出来放在一起

### 4.5 threading

> 详见 [/Exercise items/003_草民网](https://github.com/Mr-z1207/Python-test/tree/master/Exercise%20items/%E7%88%AC%E8%99%AB/003_%E8%8D%89%E6%B0%91%E7%BD%91)

创建多线程，对很多个数据的爬取很有用

### 4.6 urllib 和 HTMLParser

urllib提供了一系列用于操作URL的功能。具体。。度娘吧
Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码。具体。。也是度娘吧
还是requests 和 parsel 好用。。。

### 4.7 email 和 smtplib

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

## 五、第三方模块

### 5.1 requests

requests。它是一个Python第三方库，处理URL资源特别方便。

要通过GET访问一个页面，只需要几行代码

```python
response = requests.get('https://www.douban.com/', headers=headers)
```

需要传入HTTP Header时，我们传入一个dict作为headers参数：

```python
response = requests.get('https://www.douban.com/', headers=headers)
```

获取正确的编码

```python
response.encoding = response.apparent_encoding
```

携带参数

```python
params = {'key': 'value'}

r = requests.get('http://127.0.0.1', params=params)
```

### 5.2 parsel

parsel 是scrapy 出品的，也是scrapy内置的选择器包含re、css、xpath选择器,依赖lxml,比起bs4好用的不要不要的。

示例：

```python
from parsel import Selector
import requests

url = "https://news.baidu.com/"
body = requests.get(url).text

# 先创建一个selector
selector = Selector(text=body)

# 然后就可以用正则、css选择器，对他为所欲为了
title = selector.css("title::text").extract_first()
```

详见 /Exercise items/003_草民网

### 5.3 pygame

Pygame更致力于2D游戏的开发，也就是说，你可以用Pygame写一个植物大战僵尸，但是写一个魔兽世界则相当困难
详见 \python-project\My Bird

### 5.4 tkinter

这是一个创建窗口的第三方库，详见 /Exercise items/002_酷我爬歌

### 5.5 webbrowser

在浏览器打开链接