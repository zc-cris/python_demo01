# zc-cris

'''
    python中常用的三种序列化格式：
        json：通用的序列化格式，只有很少的一部分python数据类型能够通过json转化成字符串,可以使用json 序列化的数据类型：数字，字符串，列表，字典，元祖（当成列表处理）
        pickle：所有的python数据类型都可以转化为字符串；pickle序列化的内容只有python才可以理解，且部分反序列化依赖python代码
        shelve：python3 推出，序列化句柄，使用句柄来直接操作，非常方便，可以查看文档
'''
import json

info = {'name': 'cris', 'age': 12}
# 序列化
dumps = json.dumps(info)
print(dumps)  # {"name": "cris", "age": 12}

# 反序列化
loads = json.loads(dumps)
print(loads)  # {'name': 'cris', 'age': 12}

# 使用json的dump和load 向文件写数据和读数据
# with open('序列化文件','w',encoding='utf-8') as file:
#     json.dump(info,file)

# with open('序列化文件', encoding='utf-8') as file:
#     load = json.load(file)
#     print(type(load), load)  # <class 'dict'> {'name': 'cris', 'age': 12}


# 如果想要分次将数据转为字符串写入到文件中，可以结合文件操作和dumps，loads，绕开dump和load（一次性操作）
infos = [{'name': 'cris'}, {'name': 'james'}, {'name': 'curry'}]
# with open('序列化文件', 'w') as file:
#     for i in infos:
#         file.write(json.dumps(i) + "\n")

with open('序列化文件', encoding='utf-8') as file:
    for i in file:
        json_loads = json.loads(i.strip())
        print(json_loads, type(json_loads))

# pickle 同json，只是可以序列化python中所有的数据类型，注意的是：序列化数据到文件中，需要以'wb'和‘rb’ 的形式来操作文件
