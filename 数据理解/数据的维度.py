# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:58:44 2018

@author: student02
"""

from pandas import read_csv
a ='q.csv'
b = ['1','2','3','4']
data = read_csv(a ,names = b)
print(data.dtypes) #显示数据的属性和类型