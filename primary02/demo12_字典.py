# _Author: zc-cris

# 数据类型：
'''
    不可变数据类型：元组，str，int，bool      可哈希
    可变数据类型：list，字典，集合 set        不可哈希

    dict（字典）：
    1. key 必须是不可变数据类型，即可哈希的，因为需要根据哈希值去查询对应的键然后拿到 value，键的 hash 值就不能变
    2. value 随意数据类型
    3. 可以用来存储大量的有对应关系的数据，类似 java 的 map
'''

cris = {'age': 23, 'name': 'cris', 'sex': 0}
print(cris)

# 增和改(字典有键则改，没有就新增)
cris['high'] = 180
cris['age'] = 21
print(cris)

# setdefault 方法，有键不做任何修改，没有则添加
cris.setdefault('high', 178)
cris.setdefault('weight', 140)
print(cris)

# dic1.update(dic2),将 dic2中的内容同步到 dic1中，相同的键覆盖，没有则添加
man = {'address': '北京', 'age': 32}
cris.update(man)
print(cris)  # {'age': 32, 'name': 'cris', 'sex': 0, 'weight': 140, 'address': '北京'}

# 删除,pop() 根据键删除，有返回值（value),并且可以设置 pop(键，message)：如果要删除的键值对不存在，显示 message 避免报错
print(cris.pop('high'))
print(cris.pop("hhh", None))  # None

# del cris
# cris.clear()

# 查询
# 查询单个首选，如果字典没有对应的键，也不会报错，而是返回 None
name = cris.get("name1")
print(name)

# 遍历查询
print(cris.keys())  # 键列表  dict_keys(['age', 'name', 'sex', 'weight', 'address'])
print(cris.values())  # 值列表   dict_values([32, 'cris', 0, 140, '北京'])
print(
    cris.items())  # 键值对元组列表   dict_items([('age', 32), ('name', 'cris'), ('sex', 0), ('weight', 140), ('address', '北京')])

# 默认循环所有的 key 列表
for i in cris:
    print(i)

# 循环所有的 value 列表
for i in cris.values():
    print(i, end="---")

for i in cris.items():
    print(i)  # ('age', 32)...

# 参考下面的变量赋值
for k, v in cris.items():
    print(k, v)  # age 32

# 变量之间的交换和取值
a, b = 1, 2
a, b = [1, 2]
a, b = ("c", "b")
print(a, b)
a, b = b, a
print(a, b)
