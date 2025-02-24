# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 一些集合的常见用法
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}   # 创建一个集合
print("集合是一个无序的不重复元素序列", basket)                      # 这里演示的是去重功能
# {'orange', 'banana', 'pear', 'apple'}
# 两个集合做减法,下面的表示集合set_1存在而集合set_2中不存在的元素
set_1 = set([11, 22, 33])
set_2 = set([22, 33, 44, 'a'])
print(set_1 - set_2)     # {11}
# 获取两个集合中包含的所有元素，重复元素只显示一次
print(set_1 | set_2)   # {33, 22, 11, 'a', 44}
# 使用set集合获取两个列表中相同的元素
print(set_1 & set_2)    # 求两个集合中的相同元素  {33, 22}
print(set_1 ^ set_2)    # {11, 44, 'a'} 不同时存在于两个集合中的元素
# 列表 集合
l1 = [11, 22, 33]
l2 = [22, 33, 44, 'a']
l = l1 + l2
print(l)    # 连个列表拼接在一起 [11, 22, 33, 22, 33, 44, 'a']

t = set(l)     # 把列表转化成集合，也就是用set函数创建一个集合
print(type(t))
print(set(l))     # 用集合去掉了重复元素  {33, 11, 44, 'a', 22}

print(set(l1) & set(l2))    # 用&操作，取出集合中相同的元素 {33, 22}

# TODO: set comprehension
test = ['beijing', 'shanghia', 'tianjin', 'beijing', 'hebei', 'qinhuangdao']
res1 = [x + 'a' for x in test]
print(res1)
res2 = {x + 'a' for x in test}    # use curly braces for set
print(res2)
