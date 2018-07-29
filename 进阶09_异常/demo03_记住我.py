# zc-cris
import json

file_name = 'remember_me.json'


def func():
    '''结合json 模块完成记住用户的case'''
    try:
        with open(file_name) as file:
            print(json.load(file) + " 欢迎回来！")
    except:
        name = input("请输入你的名字:")
        with open(file_name, 'w') as file:
            json.dump(name, file)
        print("i will remember u! %s" % (name))


func()
