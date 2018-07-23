# zc-cris

'''
    基础的列表推导式：[每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]        # 遍历数据并处理每个数据
    完整的列表推导式：[满足条件的元素相关操作 for 元素 in 可迭代数据类型 if 元素判断条件]  # 筛选处理
'''

# 最快的方式求出30以内可以被3整除的数字
numbers = [i for i in range(30) if i % 3 == 0]
print(numbers)

# 求出30以内所有能被3整除的数的平方
numbers = [i * i for i in range(30) if i % 3 == 0]
print(numbers)

# 嵌套列表推导式
names = [i for i in ['cris', 'james', 'harden'] if 's' in i]
print(names)

# 进阶的列表推导式(不推荐这样写，可读性太差)
names = [['scripts', 'sneak', 'kass'], ['simith', 'scris', 'jasms']]  # ['cris', 'james']
result = [name for name_list in names for name in name_list if name.count('s') == 2]
print(result)  # ['scripts', 'kass', 'scris', 'jasms']

# 拓展：字典推导式
# 将字典的键值对 对调
info = {'name': 'cris', 'age': 23}
info = {info[k]: k for k in info}
print(info)  # {'cris': 'name', 23: 'age'}

# 集合推导式
# 求数字的平方并去重
result = {x * x for x in [-1, 1, 2]}
print(result)  # {1, 4}
