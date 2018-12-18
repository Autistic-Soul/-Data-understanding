# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:58:44 2018

@author: student02
"""
#查看数据的分布情况
from pandas import read_csv
a ='q.csv'
b = ['1','2','3','4']
data = read_csv(a ,names = b)
print(data.groupby('1').size()) #‘1’表示“b”中的“1”