# _Author: zc-cris


def str_length(string):
    i = 0
    for a in string:
        i += 1
    return i


length = str_length("cris")
print(length)


# 函数的返回值    return 除了返回值，还可以结束函数的运行
# 没有返回值     默认返回 None
# 一个返回值
# 多个返回值     多个返回值接收时使用对应数量的变量来接收；如果使用一个变量接收，得到的就是一个元组

def fun():
    return 1, "cris"


a, b = fun();
print(a, b)
c = fun();
print(c)  # (1, 'cris')


# 调用函数的时候，可以按照位置传递实参，也可以按照形参的名字传递实参，混着用也可以（不建议）
# 位置参数：调用函数必须要传递实参
# 默认参数：函数定义的时候已经给形参确定了默认值，调用函数如果不给这个形参传递实参，那么使用默认值
# 形参的位置：位置参数，*args，默认参数，**kwargs

def student(name, sex='男'):
    print('名字：{}，性别：{}'.format(name, sex))


student('james')  # 名字：james，性别：男
student('xixi', '女')  # 名字：xixi，性别：女


# 可变形参/动态参数，类似 java 的... 函数默认将多个参数组合成一个元组处理，按照关键字传递的形参就无法组合了
def sum(*args):
    n = 0
    for i in args:
        n += i
    return n


i = sum(1, 2, 3, 4)
print(i)


# 第二种动态参数传递方式：将序列的每个元素传递给动态参数再组合成元组
def sum(*args):
    print(args)


names = ['cris', 'alex', 'james']
sum(*names)  # ('cris', 'alex', 'james')


# 如果是需要传递不确定数量的关键字实参，那么需要使用**kwargs 来定义形参，且可以和*args 组合接收所有的参数（*args 必须在第一位）

def func(**kwargs):
    print(kwargs)


func(a=1, b='work', c=1)  # {'a': 1, 'b': 'work', 'c': 1}

# 传递命名可变形参的第二种方式: 将字典每个键值对拿出来传递
names = {'name': 'cris', 'age': 12}
func(**names)  # {'name': 'cris', 'age': 12}


# 最终函数定义效果
def fun(a, b, *args, name='cri', **kwargs):
    pass

# 函数的注释：''' xxx '''
