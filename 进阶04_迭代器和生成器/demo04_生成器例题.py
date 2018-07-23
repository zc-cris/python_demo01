# zc-cris

# 模拟每天传入一个值，然后计算所有已传入值之和/总天数的 均值
def generator():
    sum = 0
    count = 0
    avg = 0
    while 1:
        avg = yield avg
        count += 1
        sum += avg
        avg = sum / count


g = generator()
g.__next__()
result = g.send(10)
print(result)
result = g.send(20)
print(result)


# 将上面的生成器用装饰器装饰一下会是什么样？
# 如果用户调用我们写的生成器还需要调用__next__()激活，为什么不把这个步骤放进装饰器里呢？用户只关注他想要调用的函数即可
def generator_wrapper(func):
    def inner(*args, **kwargs):
        g = func()
        g.__next__()
        return g

    return inner


@generator_wrapper
def generator():
    sum = 0
    count = 0
    avg = 0
    while 1:
        avg = yield avg
        sum += avg
        count += 1
        avg = sum / count


g = generator()
result = g.send(10)  # 10
print(result)
print(g.send(50))  # 50
