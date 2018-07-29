# zc-cris
from func_name import name_handle

while 1:
    print("只要输入q，即可退出程序")
    first_name = input("请输入你的first_name: ")
    if first_name.lower() == 'q':
        break
    last_name = input("请输入你的last_name: ")
    if last_name.lower() == 'q':
        break

    full_name = name_handle(first_name, last_name)
    print("你的格式化后的名字是：%s" % (full_name))
