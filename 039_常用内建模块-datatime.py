# datetime是Python处理日期和时间的标准库。
# 获取当前日期和时间
from datetime import datetime, timedelta
now = datetime.now()
print(now)

# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime
time = datetime(2018, 12, 12, 13, 42, 32, 32133)
print(time)

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
tsTime = time.timestamp()
# tsTime = datetime.timestamp(time) 也可以
print(tsTime)
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
print(datetime.fromtimestamp(tsTime))
# 被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(tsTime))

# str转换为datetime
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
time = datetime.strptime('2019-11-11 23:42', '%Y-%m-%d %H:%M')
print(time)
# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类
newTime = now + timedelta(hours=10)
print(newTime)
