# 九九乘法表

a = 1
while a <= 9:
    b = 1           # 外围的每次循环需要将 b 重新设置为1
    while b <= a:
        print(b, "*", a, "=", b*a, end=" ")
        b += 1
    print()
    a += 1
