# zc-cris

def generator():
    a = 'ajaf'
    b = '1234'
    for i in a:
        yield i
    for c in b:
        yield c


g = generator()
for i in g:
    print(i)


# 以上格式可以使用python3 以后的新语法替代
def generator():
    a = 'abcd'
    b = '1234'
    yield from a
    yield from b


g = generator()
for i in g:
    print("------", i)
