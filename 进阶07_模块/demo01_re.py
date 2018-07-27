# zc-cris

'''
    常用的量词匹配：?,+,*，{n,m} (默认是贪婪匹配，即尽可能的按照数量最大的值去匹配)
    如果在量词后面加上?,则是惰性匹配，即尽可能的按照数量最小的去匹配（非贪婪匹配）
    <.*>---> <232>323<faf>  回溯算法找最后一个>
    <.*?>---> <232> <faf>   只要匹配到一个> 即返回一个对应的数据
'''
import re

print(r'\t')  # \t
print(r'\n')  # \n

# findall: 返回所有满足条件的结果，放在列表中
findall = re.findall('[a-z]+', "abc cris,simida")
print(findall)  # ['abc', 'cris', 'simida']

# search: 从前往后匹配，只要找到第一个满足的就返回，返回的变量需要调用group才可以拿到结果，没有满足的就返回None
search = re.search(' [a-z]+', "cris jjj fal")
if search:
    print(search.group())  # cris

# match: 从第一个字母开始匹配，如果无法匹配则返回None
search = re.match('[a-z]+', "cris jjj fal")
if search:
    print('---', search.group())

# finditer: 返回满足所有格式的数据的迭代器
finditer = re.finditer('\d', '234cfafa9')
print(next(finditer).group())  # 2
print(next(finditer).group())  # 3
print([i.group() for i in finditer])  # ['4', '9']
# for i in finditer:
#     print(i.group())


# compile
re_compile = re.compile('\d{3}')
compile_search = re_compile.search('21')
if compile_search:
    print(compile_search.group())  # 不执行

# 切割: 先按照a进行切割，然后将结果再按照b进行切割
string = 'abcd'
split = re.split('[ab]', string)
print(split)  # ['', '', 'cd']

# sub：替换,可以控制替换的次数
sub = re.sub('\d', 'A', '1234', 1)
print(sub)  # A234

# subn: 返回替换的结果和共替换了多少次
subn = re.subn('\d', 'A', '1234')
print(subn)  # ('AAAA', 4)
