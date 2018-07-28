# zc-cris

import time

print(time.time())  # 时间戳

# 时间的格式化（时间---》字符串）
print(time.strftime("%Y-%m-%d %X"))  # 2018-07-27 13:07:10
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2018-07-27 13:07:10
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(3000000000)))  # 2920-08-30 13:20:00

print(time.strftime("%Y/%m/%d %H-%M-%S"))  # 2018/07/27 13-07-10

print(time.localtime())  # 命名元祖结构的时间
print(time.localtime().tm_year)

# 字符串时间的格式化（字符串--》时间）
strptime = time.strptime('2017-12-12', '%Y-%m-%d')
print(strptime)
# time.struct_time(tm_year=2017, tm_mon=12, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=346, tm_isdst=-1)
