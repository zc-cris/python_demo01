# _Author: zc-cris


# 如果默认参数是一个可变数据类型，那么每次调用这个函数的时候，如果不给默认参数传值，那么共用这个可变数据的参数(有点像 java 的静态变量)
# 示例：
def func(names=[]):
    names.append(1)
    print(names)


func()  # [1]
func()  # [1, 1]
func()  # [1, 1, 1]
func(names=[])  # [1]
