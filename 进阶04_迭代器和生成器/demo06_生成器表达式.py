# zc-cris

'''
    列表推导式：快速生成有规律的列表，代替for循环来往列表添加数据，直接生成列表数据
'''

# 最简单的列表推导式
print([i for i in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 有规律的列表推导式
names = []
for i in range(5):
    names.append("cris%s" % i)

print(names)

# 比上面少写了两行代码，更加简便
names = ['cris%s' % i for i in range(5)]
print(names)

# 生成器表达式（实现简单的功能）;返回的是一个生成器，比列表表达式好的地方在于不占用内容，可控制执行的流程
result = (i for i in range(5))
print(result)
for i in result:
    print('----', i)
