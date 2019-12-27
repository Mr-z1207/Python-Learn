# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面
# Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    # handle_starttag(tag, attrs)：识别HTML的开始标签，例如<html>、<title>、<body>、<div>等。
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    # handle_endtag(tag)：识别HTML的结束标签，例如</html>、</body>、</div>、</p>等。
    def handle_endtag(self, tag):
        print('</%s>' % tag)

    # handle_startendtag(tag, attrs)：识别没有结束标签的HTML标签，例如<img />等。
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    # handle_data(data)：识别HTML标签内容，例如“<p>Test</p>”中的Test。
    def handle_data(self, data):
        print(data)

    # handle_comment(data)：识别HTML中的注释内容，一般是“<!-- 注释 -->”中的注释内容。
    def handle_comment(self, data):
        print('<!--', data, '-->')

    # 处理一些特殊字符，以&开头的，比如 &nbsp;
    def handle_entityref(self, name):
        print('&%s;' % name)

    # 处理特殊字符串，就是以&#开头的，一般是内码表示的字符
    def handle_charref(self, name):
        print('&#%s;' % name)


# handle_decl         处理<!开头的，比如<!DOCTYPE html>”
# handle_pi           处理形如<?instruction>的东西
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
