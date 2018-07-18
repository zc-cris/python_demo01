# _Author: zc-cris

# 用户注册
print("用户注册中...")
name = input("注册你的账号，请输入用户名：")
password = input("请输入密码:")

if name.strip() == '' or password.strip() == '':
    print("格式错误，请不要输入空字符串")
else:
    with open("info.txt", mode='w+', encoding="utf-8") as file:
        file.write(name + "=" + password)

# 用户登录
print("用户登录中...")
k = 0
with open("info.txt", mode='r+', encoding="utf-8") as file:
    # 如果分行保存用户名和密码，读取的时候就使用 for 循环读取每行文本,使用 strip 方法去空格和换行符
    info = file.readline().split("=")
    right_name = info[0]
    right_password = info[1]
while 1:
    k += 1
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name == right_name and password == right_password:
        print("登录成功！")
        break
    else:
        if k == 3:
            print("你已经输错三次了，请等10分钟后再来登录")
            break
        else:
            print("用户名或密码错误，请重新登录")
