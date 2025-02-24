#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# qq群：144081101 591302926  567351477
# CreateDate: 2018-06-07
# mix.py

import pandas as pd

df = pd.read_csv(r"../data/gapminder.tsv", sep='\t') 

# 混合选取
print("\n\nloc选取坐标")
print(df.loc[42, 'country'])    # 选择第42行，country这列对应的元素

print("\n\niloc选取坐标")
print(df.iloc[42, 0])        # 选择第42行，第0列对应的元素

print("\n\nloc选取子集")    # 逗号前的参数是行，逗号后的参数表示选取的列
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])