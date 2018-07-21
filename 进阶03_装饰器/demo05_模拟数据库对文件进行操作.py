# _Author: zc-cris

# 测试语法
print("cirs".index('i'))  # 1
print("i love you".index('love'))  # 2
for i in range(2):
    for i in 'cris':
        print(i, end="\t")
    print()


# 如果是带* 的指定条件的查询：要么是=,<,> 查询
def methodB():
    global employee_file, first_line, index, i, line
    with open('employees', encoding='utf-8') as employee_file:
        first_line = employee_file.readline().split(',')
        index = first_line.index(key_word)
        if operator == '=':
            for i in employee_file:
                line = i.split(',')
                if line[index] == key_content:
                    print(i)
        elif operator == '<':
            for i in employee_file:
                line = i.split(',')
                if int(line[index]) < int(key_content):
                    print(i)
        elif operator == '>':
            for i in employee_file:
                line = i.split(',')
                if int(line[index]) > int(key_content):
                    print(i)


# 如果是带* 的 like 查询走这个方法
def methodA():
    global select_condition, key_word, key_content, employee_file, first_line, index, i, line
    select_condition = select_condition.split(" ")
    key_word = select_condition[0]
    key_content = select_condition[2]
    with open('employees', encoding='utf-8') as employee_file:
        first_line = employee_file.readline().split(',')
        index = first_line.index(key_word)
        for i in employee_file:
            line = i.split(',')
            if key_content in line[index]:
                print(i)


# 根据查询内容进行符合条件的打印输出方法
def standard_print():
    global i
    for i in indexs:
        print(line[i], end='\t')
    print()


# 对employees 文件里面的员工进行查询
while 1:
    content = input("请输入你的查询语句，输入 q 则退出：")
    if content.strip().lower() == 'q':
        break

    # 1. 需要对查询条件和查询内容提取出来
    select_content = content[6:content.index('where')].strip()
    select_condition = content[content.index('where') + 5:].strip()
    # print(select_content, select_condition)
    # 2.1 分类处理
    # 如果查询所有内容，查询条件有两种：like 查询和<,=,> 查询
    if "*" in select_content:
        if 'like' in select_condition:
            methodA()

        else:
            select_condition = select_condition.split(" ")
            key_word = select_condition[0]
            operator = select_condition[1]
            key_content = select_condition[2]
            methodB()

    # 2.2 分类处理
    # 如果指定查询内容，查询条件有两种：like 查询和<,=,> 查询
    else:
        select_content = select_content.split(',')

        if 'like' in select_condition:
            select_condition = select_condition.split(" ")
            key_word = select_condition[0]
            key_content = select_condition[2]

            with open('employees', encoding='utf-8') as employee_file:
                first_line = employee_file.readline().split(',')
                first_line[-1] = first_line[-1].strip()
                indexs = []
                for print_name in select_content:
                    print(print_name, end="\t")
                    indexs.append(first_line.index(print_name))
                print()
                index = first_line.index(key_word)
                for i in employee_file:
                    line = i.split(',')
                    if key_content in line[index]:
                        standard_print()
        else:
            select_condition = select_condition.split(" ")
            key_word = select_condition[0]
            operator = select_condition[1]
            key_content = select_condition[2]
            with open('employees', encoding='utf-8') as employee_file:
                first_line = employee_file.readline().split(',')
                first_line[-1] = first_line[-1].strip()
                indexs = []
                for print_name in select_content:
                    print(print_name, end="\t")
                    indexs.append(first_line.index(print_name))
                print()
                index = first_line.index(key_word)
                if operator == '=':
                    for i in employee_file:
                        line = i.split(',')
                        if line[index] == key_content:
                            standard_print()
                elif operator == '<':
                    for i in employee_file:
                        line = i.split(',')
                        if int(line[index]) < int(key_content):
                            standard_print()
                elif operator == '>':
                    for i in employee_file:
                        line = i.split(',')
                        if int(line[index]) > int(key_content):
                            standard_print()
