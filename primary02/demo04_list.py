# _Author: zc-cris


a = ["cris", "james", "harden", "curry", "durant"]

print(a[1])
print(a[0:2])  # 切片，就是取出指定范围的元素，左闭右开
print(a[0:])  # 取出当前列表的所有元素
print(a[0:-1])  # 取出列表从第一个元素开始直到倒数第二个元素
print(a[0::2])  # 从左到右隔一个再取，最后一个2为步长，默认为1
print(a[4::-2])  # 步长的正负号决定遍历的方向：正号表示从左往右；负号表示从右往左；数值表示间隔
print(a)
