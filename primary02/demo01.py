# python 的字符串格式化

name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
job = input("请输入你的职业：")

msg = '''
    ------- the message of %s -----
    name: %s
    age: %d
    job: %s
    -------------------------------
''' % (name, name, age, job)

print(msg)
