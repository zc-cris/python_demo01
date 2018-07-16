# 嵌套 while 循环计算5轮数字：从1-10
a = 0
b = 0
while a < 5:
    a += 1
    b = 0
    print("第", a, "轮",end=":")
    while b < 10:
        b +=1
        print(b, end=" ")
    print()     # 打印换行（默认换行符结尾）