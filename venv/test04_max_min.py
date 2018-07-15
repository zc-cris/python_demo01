
a = int(input("请输入一个数字："))
b = int(input("请输入一个数字："))
c = int(input("请输入一个数字："))

max = 0
if a > b:
    max = a if a > c else c
    print("最大值：",max)
elif a == b:
    max = a if a > c else c
    print("最大值：",max)

else:
    max = b if b > c else c
    print("最大值：",max)
