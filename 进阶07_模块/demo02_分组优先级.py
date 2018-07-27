# zc-cris

import re

# 关于group 方法，可以拿到分组里匹配的数据,re的search 和 match 方法返回的对象都有group 方法，但是findall就没有了
re_search = re.search('^[1-9](\d{14})(\d{2}[0-9x])?$', '870903399301033810')
print(re_search)  # <_sre.SRE_Match object; span=(0, 18), match='870903399301033810'>
print(re_search.group(1))  # 70903399301033
print(re_search.group(2))  # 810

# findall优先返回分组匹配的数据，如果想要返回整个数据，需要使用？取消分组优先级
re_findall = re.findall('www.(?:cris|baidu).com', 'www.cris.com')
print(re_findall)  # ['cris']  --> ['www.cris.com']

# 关于split 方法的分组优先级
string = 'ab2ca4d'
split = re.split('\d', string)
print(split)  # ['ab', 'ca', 'd']
re_split = re.split('(\d)', string)
print(re_split)  # ['ab', '2', 'ca', '4', 'd']  保留切割的正则数据
