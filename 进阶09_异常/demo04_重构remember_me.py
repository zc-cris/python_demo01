# zc-cris
import json
import os


def file_exist(file_name):
    '''判断文件是否存在'''
    if os.path.exists(file_name):
        return True
    return False


def save_new_name(file_name):
    '''文件不存在就创建文件并记录用户输入的名字'''
    name = input("请输入你的名字：")
    with open(file_name, 'w') as file:
        json.dump(name, file)
    print("i will remember u，%s" % (name))


def say_hello():
    file_name = 'refactor_remember_me.json'
    exist = file_exist(file_name)
    if exist:
        with open(file_name) as file:
            print(json.load(file) + "，欢迎回来！")
    else:
        save_new_name(file_name)


say_hello()
