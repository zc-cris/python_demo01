# _Author: zc-cris

# 计算多个数字的和
def my_sum(*args):
    total = 0
    for i in args:
        total += i
    return total


number = my_sum(1, 3, 4, 5)
print(number)


# 获取传入的列表或者元组的奇数索引的值，组合成新的列表返回
def func(arg):
    new_list = []
    for i in arg:
        if arg.index(i) % 2 != 0:
            new_list.append(i)
    return new_list


l = func(['jack', 'cris', 1, 3, 88])
print(l)  # ['cris', 3]


# 方法二：最简单优雅的方式（切片）
def func(arg):
    return arg[1::2]


print(func(['jack', 'cris', 1, 3, 88]))  # ['cris', 3]
print(func(('jack', 'james', 2, 4)))  # ('james', 4)


# 通过函数判断用户输入的字符串，列表，元组的长度是否大于5
def func(x):
    return len(x) > 5


if func("crisss"):
    print("长度大于5")


# 判断列表的长度是否大于2，如果大于2，那么返回该列表的前两个元素
def func(x):
    return x[0:2]


print(func([1, 2, 3, 4]))


# 代码优化：计算传入字符串的数字，字母，空格，以及其他的个数，并返回
def calculator(x):
    dic = {'num': 0, 'alpha': 0, 'space': 0, 'other': 0}
    for i in x:
        if i.isdigit():
            dic['num'] += 1
        elif i.isalpha():
            dic['alpha'] += 1
        elif i.isspace():  # 判断空格 isspace（）方法
            dic['space'] += 1
        else:
            dic['other'] += 1
    return dic


print(calculator("c323ris   "))


# 判断用户输入的字符串是否有空格，类别和元祖是否有空元素
# 'cris   hello', [1,2,'',[],()]
def judge(x):
    if type(x) is str and x:  # '' 就是 False，有内容的字符串才是 True
        if ' ' in x:
            return True
        return False
    elif type(x) is list or type(x) is tuple:
        for i in x:
            # if (not type(i) is int) and len(i) == 0:
            if not i:  # [],(),''都是 False
                return True
    elif not x:
        return True

    return False


print(judge("cris ,heha!"))  # True
print(judge(''))  # True
print(judge([1, 2]))  # False


# 检查传入的字典的每个 value 的长度，如果大于2，那么仅保留前两个长度的内容，返回给调用者
# 注意：字典的 value 必须是 str 类型或者列表
def my_func(x):
    if type(x) is dict:
        for k, v in x.items():
            if len(v) > 2:
                v = v[0:2]
                x[k] = v
        return x
    else:
        return None


print(my_func({1: ['cris', 12, 33], 2: 'jack'}))
