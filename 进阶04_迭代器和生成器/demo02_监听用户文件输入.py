# # _Author: zc-cris

# 监听文件输入有问题，无法感应用户输入的内容？？？
def track_file(file_name):
    f = open(file_name, encoding='utf-8')
    while True:
        line = f.readline()
        if line.strip():  # 如果当前行是有内容的
            yield line.strip()


g = track_file('file')  # 返回一个生成器对象
for i in g:  # 执行生成器
    if 'cris' in i:
        print("---", i)

# f = open('file',encoding='utf-8')
# while True:
#     line = f.readline()
#     if line:
#         print(line.strip())
