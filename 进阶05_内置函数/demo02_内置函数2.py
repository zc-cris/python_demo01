# zc-cris

# reverse
names = ['cris', 'james']
names.reverse()
print(names)

iterator = reversed(names)  # 返回的反转后的迭代器，不影响原列表
print(iterator)  # <list_reverseiterator object at 0x000001D9FD5CE2E8>
print(names)
