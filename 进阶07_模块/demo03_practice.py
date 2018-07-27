# zc-cris

'''
    给标签进行分组匹配:
        可以在分组中利用（?P<name>正则表达式）的方式来给分组规则进行别名，获取到的匹配结果可以直接使用group(’name‘)的方式来获取
        复合分组规则的匹配内容，我们称之为命名分组和引用分组；如果不想起名，可以使用序号的方式来引用分组规则（不推荐，示例：<(\w+)>\w+</\1>）
'''
import re

search = re.search('<(?P<name>\w+)>\w+</(?P=name)>', '<h2>cris</h2>')
print(search)  # <_sre.SRE_Match object; span=(0, 13), match='<h2>cris</h2>'>
print(search.group('name'))  # h2
print(search.group())  # <h2>cris</h2>
