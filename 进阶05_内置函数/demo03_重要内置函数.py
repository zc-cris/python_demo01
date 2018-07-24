# zc-cris

# zip 拉链方法，以最小长度组合各个序列对象的值
a = [1, 2, 3]
b = ['a', 'b', 'c']
iterator = zip(a, b)
for i in iterator:
    print(i)


# filter，类似java的stream API的filter，过滤函数
# 判断奇数的函数
def is_odd(num):
    return num % 2 == 1


filter1 = filter(is_odd, [1, 2, 3, 4])
print(filter1)  # <filter object at 0x000001EFEC2B8A58>
for i in filter1:
    print(i)  # 1, 3

# map,类似java的stream API 的map
map1 = map(abs, [-1, 2, -3])
print(map1)
for i in map1:
    print(i)

# sorted 生成新的已经排序好的列表，不改变原列表，sort在原列表上排序
a = [1, 3, 0, -3]
l = sorted(a)
print(a)

# 按照指定规则排序
a = ['   ', 'strffa', [23, 'cris']]
sorted1 = sorted(a, key=len)
print(sorted1)  # [[23, 'cris'], '   ', 'strffa']
