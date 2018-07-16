# _Author: zc-cris

# 字符串的切片
string = "abcdefg"

a = string[0]
print(a)  # a  第一位索引默认为0

b = string[-1]
print(b)  # g  末尾最后一位索引为-1

c = string[0:3]
print(c)  # abc（顾头不顾尾）

d = string[:]
print(d)  # 取出所有字母

e = string[0:]
print(e)  # 取出所有字母

f = string[0::2]
print(f)  # 每隔一个字母取出，步长默认是1

g = string[4:0:-1]
print(g)  # edcb -1表示从后往前截取

h = string[4::-2]
print(h)  # eca

i = string[-1::-1]
print(i)  # 倒着取出所有字母

k = string[::-1]
print(k)  # 倒着取出所有字母
