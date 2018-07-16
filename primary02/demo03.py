# _Author: zc-cris

_name = "cris"
_password = 123

for i in range(2):

    name = input("请输入登录名：")
    password = int(input("请输入密码："))

    if _name == name and _password == password:
        exit("welcome %s comming..." % name)
    else:
        print("loginName or password is wrong!")

# a = 0
# while a < 2:
#     name = input("请输入登录名：")
#     password = int(input("请输入密码："))
#
# if _name == name and _password == password:
#     exit("welcome %s comming..." % name)
# else:
#     print("loginName or password is wrong!")
# a += 1
