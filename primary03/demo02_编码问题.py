# _Author: zc-cris


'''
    ascii:
        A ： 8位，一个字节表示

    unicode:
        A : 32位，四个字节表示
        中文：32位，四个字节表示

    utf-8：
        A：8位，一个字节表示
        中文：24位，三个字节表示

    gbk:
        A: 8位，一个字节表示
        中文：16位，两个字节表示

'''

# 各个编码之间的二进制数，通常不能互相转换，会有乱码
# 文件的存储和传输，不要选择 unicode 编码（占用空间）

# 简单看看 str 和 bytes 类型
a = 'cris'
b = b'cris'
print(a, type(a))  # str
print(b, type(b))  # bytes

a = '中国'
# b = b'中国'               # bytes 类型直接写中文报错
print(a, type(a))
# print(b, type(b))

# 重点：str --》 bytes ：实际上就是 unicode --》 utf-8 / gbk (默认是 utf-8)
b = a.encode()
print(b)  # b'\xe4\xb8\xad\xe5\x9b\xbd'

a = 'cris'
b = a.encode("gbk")
print(b)  # b'cris'
