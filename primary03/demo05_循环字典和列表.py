# _Author: zc-cris

# 遍历字典的时候，不允许同时删除字典中的元素
# 需求：删除字典中含有 k 的键值对
names = {'k1': 'v1', 'k2': 'v2', 'a1': 23}

# 两种方法如下：
a = []
for i in names:  # 默认遍历字典的所有 key
    if 'k' in i:
        a.append(i)
for i in a:
    # del names[i]
    names.pop(i)
print(names)  # {'a1': 23}

# 第二种方法：
names = {'k1': 'v1', 'k2': 'v2', 'a1': 23}
a = {}
for i in names:
    if 'k' not in i:
        a.setdefault(i, names[i])
names = a
print(names)  # {'a1': 23}

# 删除列表(删除奇数索引的值)
a = [1, 3, 5, 8]
b = []

for i in range(len(a)):  # for in 循环一旦执行就固定了循环次数
    # a.pop(i)                # 列表的每次操作都会对原列表产生影响，而字符串是不可变数据，每次操作字符串生成新的
    if i % 2 == 0:
        b.append(a[i])
a = b
print(a)  # [1, 5]

# 各种数据类型转换为 bool 为 False
# 0，''，[],{},(),set()

# 一旦元祖只有一个元素，那么该元祖就是该元素对应的数据类型
tu1 = (1)
tu2 = (1,)
print(tu1, type(tu1))  # 1 <class 'int'>
print(tu2, type(tu2))  # (1,) <class 'tuple'>
