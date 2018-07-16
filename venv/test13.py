# 根据用户输入的行数打印倒立的直角三角形

a = int(input("请输入行数："))
while a > 0:
    b = 0
    while a -b > 0:
        print("*",end="")
        b += 1
    a -= 1
    print()