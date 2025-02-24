# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/7/2  16:42
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
# 函数功能为取传入的多个参数中的最大值，或者传入的可迭代对象元素中的最大值。
# 默认数值型参数，取值大者；
# 字符型参数，取字母表排序靠后者。
# 还可以传入命名参数key，其为一个函数，用来指定取最大值的方法。default命名参数用来指定最大值不存在时返回的默认值。
num2 = "1314521"
print(max(x for x in range(10)))   # 取出0~9之间的最大值，输出结果为：9
print(max(num2, key=lambda x: abs(int(x))))  # 取出字符串num2中的最大数字，输出结果为：5
print(max(1, 2, 3, 4))