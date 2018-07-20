# _Author: zc-cris


import time


# time.sleep(2)       # 休眠
# print(time.time())  # 获取时间，单位为秒，同 java

# 一个简单的函数执行时间计算器
def calculate_func_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print("消耗时间：", end - start)

    return inner


def func():
    print("程序执行中...")


# calculate_func_time(func)

# 现在计算函数的执行时间，必须调用calculate_func_time 函数，有没有可能直接调用 func 函数就可以完成执行时间的功能呢？
func = calculate_func_time(func)
func()  # 我们可以通过调用 func 函数来直接完成时间的计算，但是现在的 func 其实指向的是calculate_func_time 的内部函数 inner

# 装饰器：类似于 java 的动态代理，不同的是 java 需要借助接口或者父类完成代理的功能，python 中直接通过函数即可完成，更加简洁
# 不在修改原函数的调用方式的情况下，对原函数做一些功能上的增强，而对原函数进行装饰的函数称之为装饰器：对函数进行装饰
# 装饰器本质就是闭包，或者说高级函数（函数式编程）
# 开发原则：开放封闭原则（同 java）
