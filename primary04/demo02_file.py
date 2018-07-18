# _Author: zc-cris


f = open("text.txt", mode="r+", encoding="utf-8")
print(f.read(2))  # 指定读几个字符，无论英文中文都是一个字符
f.close()

f = open("text.txt", mode="r+", encoding="utf-8")
f.seek(0)  # seek 按照字节移动光标，中文三个字节，很有可能出错，英文一个字节，没问题
print(f.read())
print(f.tell())  # 告诉光标的位置

f.seek(f.tell() - 3)  # 按照字节移动光标再读取
print(f.read())
f.close()

f = open("text.txt", mode="r+", encoding="utf-8")
# f.readline()
lines = f.readlines()  # 每一行内容当做列表中的一个元素
print(lines)
f.close()

# 按行读取文件（一般不建议全部读取出来）
f = open("text.txt", mode="r+", encoding="utf-8")
for line in f:
    print(line)
f.close()

# 省略close 操作并且一次性打开多个文件，建议使用 with 语法
with open("text", mode="r+", encoding="utf-8") as f1, open("text.txt", mode="r+", encoding="utf-8") as f2:
    print(f1.read())
    print(f2.read())
