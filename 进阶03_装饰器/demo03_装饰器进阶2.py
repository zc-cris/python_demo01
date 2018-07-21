# _Author: zc-cris

import time

# 对于有返回值的被装饰函数，需要在装饰器里面的 inner 函数手动 return，这样外界调用的时候才能获取到
from functools import wraps


def decoration_func(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("共消耗时间：", end - start)
        return result

    return inner


# 被修饰的参数类型为 *args 的函数
@decoration_func  # 这是装饰器的语法糖，类似 java 的注解，@装饰器函数名 放在被装饰函数的声明上面
def func(a, b):
    '''
    这是原函数 func 的文档注释
    :param a:
    :param b:
    :return:
    '''
    print("good morning，cris", a, b)
    return "好热啊"


result = func(1, 2)
print(result)  # 好热啊
print(func.__name__)  # func
print(func.__doc__)  # 打印 func 的文档注释
