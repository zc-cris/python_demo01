# _Author: zc-cris

from functools import wraps


# 每次函数执行前，将函数名写入到日志文件中
def logger_record(func):
    @wraps(func)
    def inner(*args, **kwargs):
        with open("log", 'a', encoding='utf-8') as file:
            # 或者打印 func.__name__
            file.write(inner.__name__ + "\r")
        result = func(*args, **kwargs)
        return result

    return inner


@logger_record
def login():
    print("登录测试")


@logger_record
def test():
    print("测试")


login()
test()
