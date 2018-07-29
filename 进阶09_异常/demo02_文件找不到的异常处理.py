# zc-cris


def func(file_name):
    '''定义一个函数，用来描述一个文本文件有多少个单词'''
    try:
        with open(file_name) as file:
            content = file.read()
            # print(content)
    except:
        print("sorry, can not find %s" % (file_name))
    else:
        split = content.split()  # 默认以空格分割字符串
        print(file_name + " hava %s word" % (len(split)))


func('abc')
func('file')
