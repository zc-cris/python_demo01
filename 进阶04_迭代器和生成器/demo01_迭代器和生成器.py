# _Author: zc-cris


# 可 for in 循环的序列型数据类型
# list，str，dict，set，tuple，f = open（），range(),enumerate
print(dir([]))  # dir 方法可以查看对应数据类型的内置函数

# 双下方法:调用+ 号其实就是调用内置的双下方法（了解）
print([1].__add__([2]))  # [1, 2]
print([1] + [2])  # [1, 2]

# 查看各种数据类型共有的内置函数（集合的交集）
result = set(dir([])) & set(dir('')) & set(dir({})) & set(dir(tuple))
print(result)

# 只要是可以被 for 循环的数据类型一定有 __iter__ 内置函数，这个函数返回的就是一个迭代器
print([].__iter__())  # <list_iterator object at 0x101fc82b0>
# 求差集（迭代器兑现相对于 [] 独有的方法）
print(set(dir([].__iter__())) - set(dir([])))  # {'__length_hint__', '__setstate__', '__next__'}


# 可迭代协议：只要含有__iter__ 函数的数据类型都是可以 for 循环的
# 迭代器协议：内部同时含有__next__,__iter__ 函数的才能是迭代器

# 生成器：一边生产，一边产出；可以分类为生成器函数或生成器表达式;生成器其实就是可控制运行流程的迭代器
# 只要含有 yield 关键字的函数都是生成器函数，yield 不能和 return 共用且只能写在函数里面,yield 可以用来返回数据和记录生成器的执行节点

def generator():
    print(1, end="---")
    yield 'a'
    print(2, end="---")
    yield 'b'


g = generator()  # 获取到一个生成器
# print(g.__next__())     # 1---a       第一次执行__next__ 生成器函数走到第一个 yield
# print(g.__next__())     # 2---b       第一次执行__next__ 生成器函数走到第一个 yield

# for 循环一次性执行生成器函数
for i in g:
    print('=====', i)  # 1---===== a   2---===== b


# 自定义一个生成器函数
def generator():
    for i in range(100000):
        yield 'cris%d' % i


generator1 = generator()  # 返回一个生成器对象
count = 0
for i in generator1:
    print(i)
    count += 1
    if count == 50:  # 先执行还是先判断，对后续结果有着细微的影响；如果先判断，这里的i == 50的循环结果就被丢弃了；
        # 先执行，然后再判断可以避免数据的丢失
        break

print(generator1.__next__())
