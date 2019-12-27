# urllib提供了一系列用于操作URL的功能。

# ####  Get  ####
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
# 例如，对百度 https://www.baidu.com 进行抓取，并返回响应
from urllib import request, parse

# urlopen 详见https://www.jianshu.com/p/63dad93d7000

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('k, v ---', '%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，
# 我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('k, v ---', '%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
print('post name to http://127.0.0.1:3000...')
name = input('name: ')
# urllib.parse 模块里的 urlencode() 方法来将参数列表转化为字符串
login_data = parse.urlencode([
    ('name', name),
])

# 测试时，先打开 ./file/043-file/server.js
req = request.Request('http://127.0.0.1:3000')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# ############  这下面看不懂。。。。。。。。。。。
# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：

proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

# urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
# 伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。
