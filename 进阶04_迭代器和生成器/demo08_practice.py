# zc-cris

# 处理文件：用户指定要查找的文件和内容，将文件中包含查找内容的每一行都输出到屏幕中
# 传统方法
def func(file_name, content):
    with open(file_name, encoding='utf-8') as file:
        for i in file:
            if content in i:
                print(i)


func('file', 'cris')
print("------------")


# 生成器（推荐）
def func(file_name):
    with open(file_name, encoding='utf-8') as file:
        for i in file:
            yield i


g = func('file')
for i in g:
    if 'cris' in i:
        print(i)
