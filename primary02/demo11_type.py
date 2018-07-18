# _Author: zc-cris

# type(xxx) == list 可用于类型判断

names = ["cris", [123, "james"], "kkk"]
for i in names:
    if type(i) == list:
        for j in i:
            print(j, end="---")
    else:
        print(i, end="---")
