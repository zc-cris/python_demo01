# zc-cris

'''
    常见的python基础数据类型：列表，元祖，字典，集合，frozenset，字符串
    计算机最常见的数据类型：队列（先进先出,FIFO）和堆栈（先进后出）
    collections 模块定义的其他数据类型如下
'''

# namedtuple：命名元祖，方便我们对数据进行定义以及属性获取，类似java中我们自己定义的类和有参构造方法，常用格式：namedtuple('名称'，[属性list])
from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print(p)  # point(x=1, y=2)
print(p.x)  # 1
print(p.y)  # 2

# 队列数据类型，如果没有数据了再取就会造成堵塞
import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())  # 0

# 双端队列,两端存取，可插入，类似java中的LinkedList，添加和删除效率高，而python的list类似java的ArrayList，查询很快
from collections import deque

de = deque()
de.append(123)
de.appendleft('cris')
de.insert(1, 'james')
print(de)  # deque(['cris', 'james', 123])
print(de.pop())  # 123
print(de.popleft())  # 'cris'

# python中我们常用的普通字典数据类型是无序的（遍历键值对的时候无法确认顺序），collections提供了有序字典
from collections import OrderedDict

ordered_dict = OrderedDict([('name', 'cris'), ('age', 23)])
print(ordered_dict)  # OrderedDict([('name', 'cris'), ('age', 23)])
print(ordered_dict['name'])  # cris

# collections 还提供了具有默认值的dict
from collections import defaultdict

d = defaultdict(list)  # 默认value是list列表
d['k1'].append([1, 2, 3])
print(d['k1'])  # [[1, 2, 3]]

# dic = dict()
# dic['k2'].append([3,2,1])       报错
# print(dic['k2'])

# dic = dict()
# print(dic['fa'])        # 报错

defaultdict1 = defaultdict(lambda: 5)  # 可以设置value的默认值
print(defaultdict1['12'])  # 5
