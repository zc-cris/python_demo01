# zc-cris

'''
    双下方法：很少直接调用的方法，一般情况下，都是通过其他语法触发
    可迭代的数据类型：遵守可迭代协议，含有__iter__ 的方法(‘——iter__’ in dir(数据))
    可迭代的数据类型一定可以被for循环
    迭代器：含有 __iter__ 和 __next__ 方法
    迭代器本生就是可以迭代的，可迭代的数据类型通过 __iter__() 方法就可以得到一个迭代器

    迭代器的特点：迭代数据，且只能取所有的数据一次，节省内存空间

    生成器：本质就是迭代器
    表现形式：生成器函数和生成器表达式
    生成器函数：
        含有yield 关键字的函数就是生成器函数
        特点：调用该函数返回一个生成器
            每次调用__next__() 方法都会取到一个值，直到取完最后一个
'''


# 定义一个生成器函数
def generator():
    for i in range(100000):
        yield i


# 得到一个生成器
g = generator()
# 遍历生成器获取数据（实际通过g.__next--()方法来取值）
for i in g:
    print(i)
    if i == 2:
        break


# 从生成器中取值的几个方法：
# 1. __next__()
# 2. for循环
# 3. 数据类型的强制转换：list(g),但是不推荐，因为会遍历迭代器将所有内容放进列表中，太占用内存

# 每次执行生成器对象的__next__()方法都会执行到下一个yield 节点为止，如果没有找到下一个yield 关键字，则报错
def generator():
    print(1)
    yield 2
    print(3)
    yield 4


generator1 = generator()
a = generator1.__next__()
print("----", a)
a = generator1.__next__()
print("----", a)


# send（）方法: 同 __next__()方法一样，也是进行到下一个yield 关键字，但是外界可以向生成器函数传递值，供生成器函数使用
# 注意：执行到最后一个yield 都不要再使用next或者send 方法了
def generator():
    num = yield 1
    num = yield 2
    print('####', num)
    yield 3


g1 = generator()
result = g1.__next__()
print(result)
result = g1.send("cris")
print(result)
result = g1.send("james")
print(result)
