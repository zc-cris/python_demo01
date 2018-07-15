death_age = 100;
name = input("请输入名字:")
age = input("请输入年龄:")

# 默认 input 输入的都是字符串类型；在 python 中如果字符串转为 int：int(xxx);如果 int 转为字符串：str(xxx)

print("你输入的名字是：",name, "你输入的年龄是：",age)
print("你还可以活：",death_age-int(age),"岁")