
number = int(input("请输入一个数字："))

# and 关键字： 条件 a and 条件b：如果 a 和 b 都为 true，整体结果才为true；一旦条件 a 为 false，直接返回 false，而不进行
# 条件 b 的判断
# if number > 5 and number < "cris":
#     print("ok")

# or 关键字：条件 a or 条件 b：如果a 和 b 任意一个条件为 true，则整体返回 true；如果 a 条件为 true，就不再进行条件 b 的判断
# if number > 5 or number < "jack" :
#     print("ok")

# not 关键字：not 条件 a 就是取条件 a 的相反值
if not number > 4:
    print("ok")
