# zc-cris

# demo1：将列表中的所有人名的末尾加上_sb
names = ['cris', 'alex', 'james']
i = map(lambda x: x + "_sb", names)  # map 返回的结果就是迭代器
for a in i:
    print(a)

# demo02：用filter将列表中的所有偶数计算出来
numbers = [1, 2, 3, 4]
iterator = filter(lambda x: x % 2 == 0, numbers)
# iterator = filter(lambda x: True if x %2 ==0 else False, numbers)
print(list(iterator))  # [2, 4]

# demo03 如下，计算购买每支股票的总价，以及过滤出单价大于1000的股票
stocks = [
    {'name': 'apple', 'shares': 100, 'price': 1000.23},
    {'name': 'samsung', 'shares': 23, 'price': 134.23},
    {'name': '长生制药', 'shares': 1, 'price': 0.23},
    {'name': '小米', 'shares': 500, 'price': 1123.23},

]
# 计算每支股票的总价
map1 = map(lambda x: {x['name']: x.get('shares') * x.get('price')}, stocks)
print(list(map1))  # [{'apple': 100023.0}, {'samsung': 3087.29}, {'长生制药': 0.23}, {'小米': 561615.0}]

# 计算所有股票的总价
total_price = 0
for i in stocks:
    total_price += i.get('shares') * i.get('price')
print(total_price)  # 664725.52

filter1 = filter(lambda x: x.get('price') > 1000, stocks)
print(list(
    filter1))  # [{'name': 'apple', 'shares': 100, 'price': 1000.23}, {'name': '小米', 'shares': 500, 'price': 1123.23}]

# # python 中的手动分页demo：divmod(被除数，除数)
# with open("file", encoding='utf-8') as file:
#     content = file.readlines()
#
# page_num = input("每页显示5条数据，请输入你要查看的页码：")
# page_num = int(page_num)
# total_pages, mod = divmod(len(content), 5)
# # 如果有余数，说明最大页数应该在商的基础上加1
# if mod: total_pages += 1
#
# if page_num > total_pages:
#     print("输入的数字大于总页数：{}".format(total_pages))
# elif page_num < 1:
#     print("请输入正确的页码")
# elif page_num == total_pages and mod:  # 如果用户查询最后一页，且最后一页内容数量不足page_num
#     for i in range(mod):
#         print(content[(page_num - 1) * 5 + i], end='')
# else:
#     for i in range(5):
#         print(content[(page_num - 1) * 5 + i], end='')
