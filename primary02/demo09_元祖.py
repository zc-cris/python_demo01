# _Author: zc-cris


# 列表的嵌套
names = ["cris", 23, ["james", "faker"]]
print(names[0][3])  # s

names[0] = names[0].capitalize()
print(names[0])

names[0] = names[0].replace("s", "jjj")
print(names)
# 或者直接修改
# names[0] = "Crisjjj"

# 连接方法 join
s = "cris"
b = "-".join(s)
print(b)

# 列表转换为字符串
names = ["kobe", "cris", "james"]
c = "+".join(names)  # kobe+cris+james, 注意列表里的元素必须都为字符串
print(c)

# 元祖不能添加， 修改和删除，但是可以查询（切片），遍历
# 如果元祖中有元素是列表，则可以crud 操作
tu = (2, 4, "cris", [23, "james"], "jj")
for i in tu:
    print(i)
tu[3][1] = tu[3][1].upper()
print(tu)  # (2, 4, 'cris', [23, 'JAMES'], 'jj')
