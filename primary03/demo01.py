# _Author: zc-cris

# = 赋值, == 比较值, is 比较内存地址, id() 得到内存地址

names = ["cris", 'james']
names1 = names
print(names is names1)
print(names == names1)
print(id(names1), id(names))  # 4367358664 4367358664

# 小数据池：对于数字来说，范围是 -5 -- 256，只要在这个范围内的数字，只开辟一个内存空间
#
a = 1000
b = 1000
print(a is b)
print(id(a), id(b))  # 4326469232 4326469232  注意：pycharm 中一样，但是命令行是不同的

s = "abc" * 3  # 字符串可以*数字，表示重复次数
print(s)  # abcabcabc
