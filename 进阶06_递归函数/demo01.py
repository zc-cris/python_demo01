# zc-cris

# 计算阶乘，直到n =1 的时候停止递归
def func(n):
    return n * func(n - 1) if n > 1 else n


print(func(3))
#
#
# result = func(4)
# print(result)
#
#
# # 二分查找算法（先排序，后查找）: 同java
# def func(numbers, key, low, high):
#     if key > numbers[high] or key < numbers[low] or low > high:
#         return '找不到key'
#     else:
#         middle = (high + low) // 2
#         if key > numbers[middle]:
#             return func(numbers, key, middle + 1, high)
#         elif key < numbers[middle]:
#             return func(numbers, key, low, middle - 1)
#         else:
#             return middle
#
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18]
#
# result = func(a, 15, 0, len(a)-1)
# print(result)

# 斐波拉契数列的双递归算法，同java,效率很慢
1, 1, 2, 3, 5, 8, 13


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


i = fib(5)
print(i)

# 使用单递归算法优化斐波拉契
count = 0


def func(n):
    global count
    count += 1

    if n == 2:
        count -= 1
        return 1, 1
    else:
        a, b = func(n - 1)
        count -= 1
        if count == 0:
            return a + b
        else:
            return b, a + b


print(func(6))
