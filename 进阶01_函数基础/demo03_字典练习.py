# _Author: zc-cris


numbers = [1, 2, 3, 4, 5, 6]
sort_container = {}

# 方法一：
for n in numbers:
    if n < 4:
        if 'k1' not in sort_container:
            sort_container['k1'] = []
        sort_container['k1'].append(n)
    else:
        if 'k2' not in sort_container:
            sort_container['k2'] = []
        sort_container['k2'].append(n)
print(sort_container)  # {'k1': [1, 2, 3], 'k2': [4, 5, 6]}

# 方法二：
for n in numbers:
    sort_container.setdefault('k1', [])
    sort_container.setdefault('k2', [])
    if n < 4:
        sort_container['k1'].append(n)
    else:
        sort_container['k2'].append(n)
print("----", sort_container)  # ---- {'k1': [1, 2, 3], 'k2': [4, 5, 6]}
