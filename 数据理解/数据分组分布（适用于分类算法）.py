# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:58:44 2018

@author: student02
"""
#计算数据集中数据属性之间的关联关系矩阵，方法：皮尔逊相关系数
from pandas import read_csv
from pandas import set_option
a ='q.csv'
b = ['1','2','3','4']
data = read_csv(a ,names = b)
set_option('display.width',100) #显示数据相关性
set_option('precision',2) #设置数据精确度
print(data.corr(method = 'pearson')) 