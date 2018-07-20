# _Author: zc-cris

# 函数的嵌套调用
def max_two_number(a, b):
    return a if a > b else b


print(max_two_number(1, 4))


def max_three_number(a, b, c):
    d = max_two_number(a, b)
    return max_two_number(d, c)


print(max_three_number(3, 1, 9))

a = 1


def outer():
    a = 2

    def inner():  # def 只定义函数，不执行
        a = 3

        def inner2():
            # global a        # 只要是声明了 global 关键字，引用的就是全局不可变数据类型的变量
            nonlocal a  # nonlocal 依次去找最近的局部变量 a，如果局部都没有，报错！
            a += 4
            print(a)

        inner2()
        print('inner 里的 a：', a)

    inner()
    print("outer 里的a：", a)


outer()
print("全局的a：", a)


# python 的函数名--》函数的内存地址，所以可将函数当做参数进行传递,当做容器的元素数据类型，当做返回值
# 所以 Python中，函数天生作为一等公民，可以很好的进行变量式的调用和传递，和 java 不同，需要借助 lambda 表达式实现
def func():
    print("cris")


func2 = func
list_funcs = [func2, func]
for i in list_funcs:
    i()


def func3(f):
    f()
    return func


a = func3(func2)
a()
