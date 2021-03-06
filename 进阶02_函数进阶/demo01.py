# _Author: zc-cris

# java 变量的作用域 类似 python 的命名空间
# 1. 内置命名空间：python解释器一启动就开启的内存，用于存放python 的内置函数
# 2. 全局命名空间：程序执行的时候开辟的内存，用于存放程序的变量名和函数名
# 3. 局部命名空间：调用函数所需要的内存，函数结束，内存释放

# 局部：可以使用全局和内置命名空间的变量
# 全局：可以使用内置命名空间的变量，但是不能使用局部的
# 内置：不可以使用全局和局部命名空间的变量
# 以上就是依赖倒置原则

# 函数的名字打印出来就是这个函数的内存地址
# 多个局部函数具有各自的局部命令空间，隔离开来

# 作用域：全局作用域（全局）和局部作用域（函数）

a = 1


# 对于不可变的数据类型
def func():
    # a = 2  在局部命名空间重新给一个变量 a 赋值，这个 a 和全局作用域的 a 不是同一个
    global a  # 不建议使用 global，类似 java 的静态变量，不要随意更改
    b = 'cris'
    print(locals())  # 可以查看局部的变量，声明在全局，等同于 globals()
    a += 1  # 修改 a 的值，需要声明 global，然后才可以修改全局变量的值


func()
print(a)  # 2
print(globals())  # 永远打印内置和全局的变量
