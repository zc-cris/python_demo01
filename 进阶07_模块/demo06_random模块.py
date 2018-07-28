# zc-cris

import random

# 默认返回大于0小于1之间的小数
print(random.random())

# 返回大于0小于3的小数
print(random.uniform(0, 3))

# 随机整数 1<= x <=3
print(random.randint(1, 3))

# 0到10之间的偶数，可设置步长
print(random.randrange(0, 10, 2))

# 随机选择一个返回
print(random.choice(['cris', 'wuyifan', 'skr']))

# 随机选择两个元素返回
print(random.sample([1, 2, 'hello'], 2))

# 打乱列表顺序
names = ['cris', 'james', 'deric']
random.shuffle(names)
print(names)
