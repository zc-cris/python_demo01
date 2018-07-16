# 用户输入指定的长和宽，打印由 * 组成的方形

length = int(input("请输入长度："))
width = int(input("请输入宽度："))

while width > 0:
    a = 0
    while a < length:
        print("*", end=" ")
        a += 1
    width -= 1
    print()