# Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦
# 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。
import requests

# 要通过GET访问一个页面，只需要几行代码
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
response = requests.get('https://www.douban.com/', headers=headers)

# 获取正确的编码
# response.encoding = response.apparent_encoding

# print(response.status_code)
print(response.text)
# print(dir(response))
print(response.encoding)


# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
# r.content

# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())


# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：

params = {'key': 'value'}
# 内部自动序列化为JSON
r = requests.post('http://127.0.0.1', json=params)


# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：

# >>> upload_files = {'file': open('report.xls', 'rb')}
# >>> r = requests.post(url, files=upload_files)
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

# 除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：

# >>> r.headers
# {Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
# >>> r.headers['Content-Type']
# 'text/html; charset=utf-8'
# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：

# >>> r.cookies['ts']
# 'example_cookie_12345'
# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：

# >>> cs = {'token': '12345', 'status': 'working'}
# >>> r = requests.get(url, cookies=cs)
# 最后，要指定超时，传入以秒为单位的timeout参数：

# >>> r = requests.get(url, timeout=2.5) # 2.5秒后超时
