# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/7/1  14:19
# 文件名称   ：demo02.py
# 开发工具   ：PyCharm

data = [10, 20, 30, 40, 50, 60, 70, 80]
strnull = ''
stradd = ''
strlin = ''
for item in data:
    strnull = strnull + str(item)  # 连接列表中的元素，间隔符为空
    stradd = stradd + '+' + str(item)  # 连接列表中的元素，间隔符为‘+’
    strlin = strlin + '<' + str(item)  # 连接列表中的元素，间隔符为‘<’
    if item == 80:
        print(item)   # 最后一个元素后面不用添加*
    else:
        print(item, end='*')  # 在输出设置间隔符为‘*’，连接各个元素, 每个元素后面以 * 作为结尾输出,加入参数end后print不换行

print(strnull)
print(stradd.lstrip('+'))
print(strlin.lstrip('<'))
