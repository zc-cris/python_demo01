# _Author: zc-cris
# 字符串常用的方法

# 首字母大写，其余字母都小写
string = "crisAbc"
a = string.capitalize();
print(a)  # Crisabc

# 所有字母大写
b = string.upper();
print(b)  # CRISABC

# 所有字母小写
c = string.lower()
print(c)  # crisabc

# 大小写翻转
d = string.swapcase()
print(d)  # CRISaBC

# 每个隔开（特殊字符或者数字）的单词首字母大写
string = 'abc DEW cAjd'
e = string.title()
print(e)  # Abc Dew Cajd

# 以字符串内容为中心进行填充
string = "python 学习日志"
a = string.center(20, "*")
print(a)  # ****python 学习日志*****

# 长度
a = len(string)
print(a)  # 11

# 以 xxx 开头
a = string.startswith('py')
print(a)  # True

a = string.startswith("on", 4, 7)  # 4表示切片的起始位置，7表示切片的结束位置（顾头不顾尾）
print(a)  # True

# 查找
a = string.find('t')
print(a)  # 2

a = string.find('k')
print(a)  # 找不到返回-1，区分大小写，支持切片

# a = string.index('k') # 几乎同 find，但是找不到会报错，首选 find

string = "   crsis  "
a = string.strip()  # 默认去字符串前后的空格，rstrip 和 lstrip
print(a)

a = string.count('s')  # 计算 s 出现的次数
print(a)  # 2

# 切割为列表
a = string.split('s')
print(a)  # ['   cr', 'i', '  ']

# format 的三种玩法: 格式化输出
string = "我叫{},今年{},爱好{},再说一遍我叫{}".format("cris", 23, "撸代码", "cris")
print(string)
string = "我叫{0},今年{1},爱好{2},再说一遍我叫{0}".format("cris", 23, "撸代码")
print(string)
string = "我叫{name},今年{age},爱好{hobby},再说一遍我叫{name}".format(age=24, name="cris", hobby="撸代码")
print(string)

# 替换，默认全部替换
string = "aaabbbcc"
a = string.replace("a", "d")
print(a)

string = "cris123"
print(string.isdigit())  # False（全部数字组成）
print(string.isalpha())  # False（全部字母组成）
print(string.isalnum())  # True（字母或数字组成）

# 字符串的包含，类似 java 中的 contains
if "cris" in string:
    print("非法字符！")
