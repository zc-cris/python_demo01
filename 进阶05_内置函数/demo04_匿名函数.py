# zc-cris

'''
    python中的匿名函数类似java中的lambda 表达式
    定义匿名函数的格式：函数名 = lambda 参数: 返回值
'''


# 正常的函数
def calculator(x, y):
    return x ** y


print(calculator(2, 3))  # 8

# 通过匿名函数修改上面格式
func = lambda x, y: x ** y
print(func(3, 2))  # 9

# demo02
dic = {'k1': 123, 'k2': 11, 'k3': 21}
print(max(dic))  # k3 默认求字典的所有key的最大值
# 如果要筛选value值最大的key
print(max(dic, key=lambda k: dic[k]))  # k1

# demo03:lambda 和 map结合
result = map(lambda x: x * x, [1, 2, 3])
for i in result:
    print(i)

# lambda和filter 结合
iterator = filter(lambda x: x > 10, [1, 2, 312])
for i in iterator:
    print(i)

# 和lambda 表达式经常一起使用的内置函数（max,min,sorted,filter,map）
# demo04：将(('a','b'),('c','d'))  --> [{'a':'c'}, {'b':'d'}]
zip1 = zip((('a'), ('b')), (('c'), ('d')))
# for i in zip1:
#     print(i)  # ('a', 'c')        ('b', 'd')

result = map(lambda x: {x[0]: x[1]}, zip1)
print(list(result))  # [{'a': 'c'}, {'b': 'd'}]
