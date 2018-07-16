# _Author: zc-cris

s = "12fa232ln9jo7"
flag = False
count = 0
number = 0
for i in s:
    number += 1
    if i.isdigit():
        flag = True
        if number == len(s):
            count += 1
    else:
        if flag:
            count += 1
            flag = False
print(count)
