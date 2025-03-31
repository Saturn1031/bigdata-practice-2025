# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 14:42:51 2025

@author: DS
"""

import csv
f_2015 = open('201502_201502_주민등록인구및세대현황_월간.csv')
f_2025 = open('202502_202502_주민등록인구및세대현황_월간.csv')
data_2015 = list(csv.reader(f_2015))
data_2025 = list(csv.reader(f_2025))

result = []
for row in data_2015[1:]:
    i = row[1].replace(',', '')
    result.append(int(i))
print(result)