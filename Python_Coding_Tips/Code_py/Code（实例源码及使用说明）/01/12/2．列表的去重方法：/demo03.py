# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/7/1  16:54
# 文件名称   ：demo03.py
# 开发工具   ：PyCharm
city = ['上海', '广州', '上海', '成都', '上海', '上海', '北京', '上海', '广州', '北京', '上海']

ncitx = list(set(city))
ncitx.sort(key=city.index)    # 按照原来列表里元素的下标来排序，即按照元素出现的顺序
print(ncitx)
