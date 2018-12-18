# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:58:44 2018

@author: student02
"""


#通过分析数据的高斯分布情况来确认数据的偏离情况
#假定数据遵循高斯分布，先计算数据的高斯偏离情况，再根据偏离情况准备数据
#计算所有数据属性的高斯分布偏离情况
#计算数据的高斯偏离
from pandas import read_csv
a ='q.csv'
b = ['1','2','3','4']
data = read_csv(a ,names = b)
print(data.skew()) #当数据接近0时，表示数据的偏差非常小 