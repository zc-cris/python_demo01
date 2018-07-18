# _Author: zc-cris

# hr 添加员工案例

employees = ["cris", "old"]

while 1:
    name = input("请输入新员工的名字，按 q 退出添加新员工名称流程：")
    if name.strip().lower() == "q":
        break
    else:
        employees.append(name)

print("当前员工为{}".format(employees))
