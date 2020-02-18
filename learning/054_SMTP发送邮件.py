# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
# mime: 模仿
from email.mime.text import MIMEText

import smtplib

# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，
# 传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# 可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录SMTP服务器
server.login(from_addr, password)
# 发邮件，由于可以一次发给多个人，所以传入一个list
# 邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#####################
#      未完待续      #
#####################
