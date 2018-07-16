# _Author: zc-cris

# str -- int
i = 2
s = str(i)
print(s, type(s))  # 2 <class 'str'>

s = "34"
i = int(s)
print(i, type(i))  # 34 <class 'int'>

# bool -- int
i = 3
b = bool(i)
print(b)  # 非0为True，0就是 False

b = True
i = int(b)  # True 为1，False 为0
print(i)

# 拓展：高效率的死循环，高于 while True
# while 1:
#     xxx

# str -- bool
s = ""
b = bool(s)  # str 有内容就是 True，""就是 False
print(b)

print(str(b))  # bool-->字符串 就是字符串类型的 False 或者 True

# 快速判断空字符串
if not s:
    print("字符串内容为空，请重新输入")
