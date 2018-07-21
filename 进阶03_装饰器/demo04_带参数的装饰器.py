# _Author: zc-cris


# 需求如下：有多个装饰器注解的函数，如何一次性控制他们的装饰和取消装饰
# 可以使用三层嵌套的装饰器，@装饰器名字（参数） 相当于先执行装饰器名字（参数）这个函数，然后将返回结果（实际的装饰器函数）当做装饰器
import time

flag = True


def wrapper_out(flag):
    def calculate_time(f):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                result = f(*args, **kwargs)
                end = time.time()
                print("消耗时间：", end - start)
            else:
                result = f()
            return result

        return inner

    return calculate_time


@wrapper_out(flag)  # 实际上是 warpper_out(flag) 这个函数的执行结果当做最终的装饰器来装饰注解下的原函数
def func(name):
    print("名字是：", name)


func('cris')


@wrapper_out(flag)
def func1():
    print("今天很热！")


func1()
