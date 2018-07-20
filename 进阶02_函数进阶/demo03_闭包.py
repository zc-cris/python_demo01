# _Author: zc-cris

# 闭包：嵌套函数中，内部函数调用外部函数的变量（不能是全局变量）
a = 2


def outer():
    a = 1

    def inner():
        print(a)  # 内部函数使用变量遵循就近原则
        print(inner.__closure__)  # 只要打印出下面的语句，证明当前函数是闭包的形式
        # (<cell at 0x101deffa8: int object at 0x1009e0980>, <cell at 0x1044adac8: function object at 0x1045070d0>)

    inner()


outer()


# 常用闭包的形式，以变量返回闭包函数，外部接受然后随时调用，外部函数的变量不会消失，避免外部函数的重复调用
def outer():
    a = 3

    def inner():
        print("cris", a)

    return inner


inner = outer()
inner()
