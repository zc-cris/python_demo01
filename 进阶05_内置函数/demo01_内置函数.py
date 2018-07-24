# zc-cris

'''
    迭代器.__next__() 等价于 next(迭代器)
    迭代器 = iter(可迭代对象) 等价于 可迭代对象.__iter__()

    数据结构：dict，list，tuple，set，str（类容器的数据类型）
    数据类型：int，bool，float ...

'''

# exec 和eval 都可以解析字符串里的python代码并执行，区别是exec内置函数没有返回值，适合简单流程控制；而eval是有返回值
# 这两个内置方法很不安全，不推荐使用，compile内置函数可以对字符串类型的python代码进行解析（exec，eval，single（交互命令））
exec('print(123)')  # 123
eval('print("cris")')  # cris

print(exec('1+2+3'))  # None
print(eval('1+2+3'))  # 6

'''
    时数：有理数和无理数（无限不循环小数）
    虚数：虚无缥缈的数（单位是i，i的平法是-1），python的单位是j
    复数（complex）：5+4j，复数不能比较大小，了解即可
'''
r = range(10)  # range()方法返回的其实是可迭代的数据，懒加载，可切片，需要取值才真正进行切片操作操作
print(r[0:3])  # range(0, 3)
print(list(r[0:3]))  # [0, 1, 2]
