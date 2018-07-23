# zc-cris

# 生成器的面试:生成器就是可控制流程的迭代器，且只能使用一次
def func():
    for i in range(3):
        yield i


g = func()
# 注意这里通过生成器表达式返回的是生成器对象（只能完整运行一次），而不是列表表达式生成的列表
g1 = (x for x in g)
g2 = (y for y in g1)
print(list(g1))  # [0, 1, 2] 执行完这行代码，意味着g1 已经不存在了
print(list(g2))  # []


# 面试题2
def add(i, n):
    return i + n


def generator():
    for i in range(4):
        yield i


g = generator()

for i in [1, 10]:
    g = (add(i, n) for n in g)

print(list(g))  # [20, 21, 22, 23]      for 循环嵌套同一个生成器，从最终的生成器g开始往回计算
