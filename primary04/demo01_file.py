# _Author: zc-cris
#
# # 存储到硬盘的二进制文件 bytes-->str，python3自动转换
# f = open("demo.txt", mode='r', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()
#
# # rb 模式常用于非文本类的文件
# f = open("demo.txt", mode='rb')
# content = f.read()
# print(content)  # b'\xe6\x90\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xe6\xa2\xa6\xef\xbc\x81ok'
# f.close()
#
# # 只写模式 w, 有源文件就覆盖内容，没有就创建并写入内容
# f = open("text.txt", mode='w', encoding='utf-8')
# f.write("湖人总冠军！")
# f.close()
#
# f = open("text.txt", mode='wb')
# f.write("行动的矮子，嘴强王者".encode("utf-8"))
# f.close()
#
# # 追加 到源文件的光标后面
# f = open("text.txt", mode='a', encoding='utf-8')
# f.write("思密达")
# f.close()

# mode = ab 类似上面，这里不再列出


# 读写模式
f = open("text.txt", mode='r+', encoding="utf-8")
print(f.read())
f.write("cris")
f.close()

# r+b 模式同上

# 写读模式 w+b 同上
f = open("text.txt", mode='w+', encoding="utf-8")
f.write("德里克")  # 光标到最后
f.seek(0)  # 移动光标到首位
print(f.read())
f.close()

# a+ 模式
f = open("text.txt", mode='a+', encoding="utf-8")
f.write("cris")  # 光标到最后
f.seek(0)  # 移动光标到首位
print(f.read())
f.close()
