"""
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
"""

a = [1, 2, 3]
b = ["xiaozhan", "beijing", "shanghai"]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)     # 打包为元组的列表
print("after zip and list", list(zipped))    # [(1, 'xiaozhan'), (2, 'beijing'), (3, 'shanghai')]
# 元素个数与最短的列表一致
l = [(1, 2), (3, 4), (5, 6)]
print(max(l))

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = [10, 11, 12]
zipped = zip(a, b, c, d)
print(list(zipped))      # [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
#
for i, m in enumerate(zip(a, b, c, d), start=1):
    print(i, ':',  m)
