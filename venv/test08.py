number = 0;

# 和 java 类似，使用 continue 关键字：当满足条件的时候就不再执行当前循环 continue 下面的代码，而是重现开始循环
while number < 5:
    number +=1      # 这里注意变量修改操作需要放在 continue 关键字前面，否则容易出现死循环
    if number == 3:
        continue
        # break
    print("当前 number：", number)
else:               # 如果是 while 循环被 break 终止或者代码出现异常，只要while 循环正常执行完毕（包括 continue）就都会执行
    print("ok")
