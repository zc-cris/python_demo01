# _Author: zc-cris


# 集合set：可变的数据类型，但是里面的元素必须是不可变的数据类型
# 集合最大的特点：无序，不能重复（类似 java 的 set）

# 创建集合的两种方式
# names = {2,3,'james',['cris',1]}        # 报错
# print(names)

names = {'cris', 'james', 'curry'}
print(names)

# 增(自动去重)
names.add("durant")
print(names)

# 迭代添加
names.update("jerry")
print(names)

# 删除:随机删除，返回删除的元素
# names.pop();
# print(names)

# 按照元素删除，没有就报错
names.remove("cris")
print(names)

# clear
# names.clear()
# print(names)        # 空集合：set（）；空字典：{}

# 删除结合
# del names

# 遍历
# for i in names:
#     print(i)

# 交集
a = {1, 2, 3, 4}
b = {1, 3, 6, 8}
print(a & b)  # {1, 3}
print(a.intersection(b))  # {1, 3}

# 并集
print(a | b)  # {1, 2, 3, 4, 6, 8}
print(a.union(b))  # {1, 2, 3, 4, 6, 8}

# 反交集：除去两个集合共有的其他元素组成一个集合
print(a ^ b)  # {2, 4, 6, 8}
print(a.symmetric_difference(b))  # {2, 4, 6, 8}

# 差集(a相对于 b 独有的元素组成一个集合)
print(a - b)  # {2, 4}
print(a.difference(b))

# 超集(a是 b 的超集)和子集(a 是 b 的子集)
print(a < b)
print(a.issubset(b))

print(a > b)
print(a.issuperset(b))

# 列表去重
numbers = [1, 1, 2, 3, 4, 3]
s = set(numbers)
numbers = list(s)
print(numbers)  # [1, 2, 3, 4]

# 将 set--》frozenset（可变数据类型--》不可变数据类型）
a = frozenset("cris")
print(a, type(a))  # frozenset({'r', 's', 'c', 'i'}) <class 'frozenset'>
