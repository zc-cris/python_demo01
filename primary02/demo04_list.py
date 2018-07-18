# _Author: zc-cris


a = ["cris", "james", "harden", "curry", "durant"]

print(a[1])  # james
print(a[0:2])  # ['cris', 'james'] 切片，就是取出指定范围的元素，顾头不顾尾
print(a[0:])  # 取出当前列表的所有元素
print(a[:])  # 取出当前列表的所有元素
print(a[0:-1])  # ['cris', 'james', 'harden', 'curry'] 取出列表从第一个元素开始直到倒数第二个元素（最后一个元素索引为-1，但是因为顾头不顾尾的原因取不到）
print(a[0::2])  # ['cris', 'harden', 'durant'] 从左到右隔一个再取，最后一个2为步长，默认为1
print(a[4::-2])  # ['durant', 'harden', 'cris'] 步长的正负号决定遍历的方向：正号表示从左往右；负号表示从右往左；数值表示间隔
print(a)  # ['cris', 'james', 'harden', 'curry', 'durant'] 对列表的切片不影响原列表

# 列表添加元素
a.append("simida")
print(a)

# 插入新元素到索引值之前
a.insert(3, "wiggins")
print(a)

# 迭代加入到列表末尾，方法参数必须为集合类型（字符串，列表等），不能是数字
a.extend([1, 2, 3])
a.extend("kobe")
print(a)  # ['cris', 'james', 'harden', 'wiggins', 'curry', 'durant', 'simida', 1, 2, 3, 'k', 'o', 'b', 'e']

# pop,按照索引删除元素，返回删除的元素，不传递参数默认删除最后一个元素
name = a.pop(2)
print(a, name)

# remove，按照元素删除
a.remove("cris")
print(a)

# clear(),清空列表内容
# a.clear()
print(a)

# 将列表从内存中删除
# del a
del a[0:2]  # 删除前两个元素
print(a)

# 按索引改
a[0] = "faker"
print(a)
# 按切片改,先删除前两个元素，然后迭代添加
# a[0:3] = "cris"
a[0:4] = [1, 2, 3, "男神"]
print(a)

# 公共方法
print(a.count(2))

print(len(a))

print(a.index(3))

a = [3, 9, 6, 4, 2, 0]
# 正向排序
a.sort()
print(a)

# 反向排序
a.sort(reverse=True)
print(a)

# 反转
a.reverse()
print(a)
