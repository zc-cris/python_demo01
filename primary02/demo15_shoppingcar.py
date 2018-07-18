# _Author: zc-cris

products = ['牙刷', '汽车', '电脑', '键盘', '西瓜']
length = len(products)
while 1:
    index = 1
    for i in products:
        print(index, i)
        index += 1

    number = input("请输入你想要看的商品序号，按 q 或 Q 退出：")
    if number.strip().lower() == 'q':
        break
    if not number.isdigit():
        print("请输入有效数字")
    else:
        number = int(number)
        if number < 1 or number > length:
            print("请输入1-{length}之间的整数".format(length=length))
        else:
            print("你选择的是：{number} {product}".format(number=number, product=products[number - 1]))

# 判断输入的字符串是否是合法的小数
# def isfloat(num):
#     if re.match('(^0\.\d+)|([1-9]\d*\.\d+)', num):
#         return True
#     else:
#         return False
#
#
# # print(isfloat("0.23"))
#
# print(type(23.23))  # float
# print(float('23.23'))  # 23.23
# # int("23.23")            # 报错
# print("23.23".isdigit())  # false, 判断字符串是否是整数
