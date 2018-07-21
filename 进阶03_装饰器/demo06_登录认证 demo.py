# _Author: zc-cris

# flag 控制登录成功后，后面的被装饰函数不再需要登录验证
flag = False
# 控制最大登录次数只能为3次，执行任何被装饰函数总共只能尝试三次登录验证
number = 0


# 登录检查函数
def login_check():
    global number
    if (number == 0):
        while number < 3:
            name = input("请输入登录名：")
            password = input("请输入密码：")
            # 模拟从数据库查询数据验证用户名和密码
            with open("info", encoding='utf-8') as file:
                for i in file:
                    i = i.split(" ")
                    if name.strip() == i[0] and password.strip() == i[1]:
                        global flag
                        flag = True
                        break
            if not flag:
                print("用户名或密码错误！")
                number += 1
            else:
                break
    else:
        print("你已经登录失败了三次，请十分钟后再尝试")


# 登录装饰器
def login_wrapper(f):
    def inner(*args, **kwargs):
        if flag:
            result = f(*args, **kwargs)
            return result
        else:
            # 执行登录流程程序
            login_check()
            if flag:
                result = f(*args, **kwargs)
                return result
            else:
                print('登录失败！，没有权限')

    return inner


@login_wrapper
def add_product():
    print("添加商品到购物车成功！")


@login_wrapper
def delele_product():
    print("删除商品成功！")


add_product()
delele_product()
