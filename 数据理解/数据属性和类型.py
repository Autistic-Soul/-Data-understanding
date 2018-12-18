# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:58:44 2018

@author: student02
"""
#可以展示数据的记录数、平均值、标准方差、最小值、下四分位数、中位数、上四分位数、最大值
from pandas import read_csv
from pandas import set_option
a ='q.csv'
b = ['1','2','3','4']
data = read_csv(a ,names = b)
set_option('display.width', 100) #前100行数据
set_option('precision', 4) #设置数据的精确度，其中“4”指保留四位小数
print(data.describe())