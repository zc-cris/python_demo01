# zc-cris

def func():
    a = input("请输入除数，或者输入q退出: ")
    if a.lower() == 'q':
        return
    b = input("请输入被除数，或者输入q退出: ")
    if b.lower() == 'q':
        return
    try:
        c = int(a) / int(b)
    except:
        print("输入有误")
    else:  # 只有当try语句块正常执行完毕，才执行else 语句块里的代码，否则执行except 语句块里的代码
        print("结果是：" + str(c))


func()
