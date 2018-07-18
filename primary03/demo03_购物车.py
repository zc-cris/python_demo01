# _Author: zc-cris


goods = [
    {'name': '西瓜', 'price': 10},
    {'name': '葡萄', 'price': 20},
    {'name': '哈密瓜', 'price': 30},
]
print(type(goods[0]))

orders = []
money = input("你有多少钱啊？")
length = len(goods)
if money.isdigit() and int(money) > 10:
    money = int(money)

    while 1:
        for k, v in enumerate(goods):
            print("序号：{}，名字：{}，价格：{}".format(k + 1, v['name'], v['price']))

        number = input("请输入你想买的商品序号：按 q 退出")
        if number.strip().lower() == 'q':
            print("欢迎下次再来啊！")
            break
        if number.isdigit() and 1 <= int(number) <= length:
            number = int(number)
            quantity = input("你要购买的是：{}，请输入你要购买的数量：".format(goods[number - 1]['name']))
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                price = goods[number - 1]['price']
                price_quantity = price * quantity
                if money - price_quantity >= 0:
                    money = money - price_quantity;
                    order = ("商品名称：{}".format(goods[number - 1]['name']), "购买数量：{}".format(quantity),
                             "花费：{}".format(price_quantity), "余额为：{}".format(money))
                    orders.append(order)
                    print("你当前购物情况为：{}".format(orders))
                else:
                    print("不好意思，你的钱不够了，当前余额为：{}，你要购买的价格为：{}".format(money, price_quantity))
            else:
                print("请输入正确的数量")

        else:
            print("请输入正确的商品序号")

else:
    print("没钱还来买东西，穷鬼！滚！")
