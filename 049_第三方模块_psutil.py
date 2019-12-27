# 获取系统信息的另一个好办法是使用psutil这个第三方模块
import psutil

# 我们先来获取CPU的信息：
# CPU逻辑数量
# cpunum = psutil.cpu_count()
# print(cpunum)
# CPU物理核心
# cpunum = psutil.cpu_count(logical=False)
# print(cpunum)
# 统计CPU的用户／系统／空闲时间：
# cputime = psutil.cpu_times()
# print(cputime)

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# for x in range(10):
#     p = psutil.cpu_percent(interval=1, percpu=True)
#     print(p)

# 物理内存
# print(psutil.virtual_memory())
# 交换内存
# print(psutil.swap_memory())

# 获取进程信息
# 通过psutil可以获取到所有进程的详细信息
# psutil.pids() 所有进程ID
print(psutil.net_connections())
