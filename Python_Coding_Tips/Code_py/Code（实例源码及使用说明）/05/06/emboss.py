# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2019/4/8  15:30 
# 文件名称   ：emboss.PY
# 开发工具   ：PyCharm
'''
  图片的浮雕效果显示
'''
from PIL import Image, ImageFilter
img = Image.open('test.jpg')           # 打开图片文件
new_img = img.filter(ImageFilter.EMBOSS)        # 设置图片筛选器
new_img.save('浮雕效果.png', 'png')             # 保存浮雕效果的图片