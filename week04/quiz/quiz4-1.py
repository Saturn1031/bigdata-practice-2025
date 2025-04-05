# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 14:42:51 2025

@author: DS
"""

#%%

import csv

f_2015 = open('201502_201502_주민등록인구및세대현황_월간.csv')
f_2025 = open('202502_202502_주민등록인구및세대현황_월간.csv')
data_2015 = list(csv.reader(f_2015))
data_2025 = list(csv.reader(f_2025))

population_2015 = []
for row in data_2015[1:]:
    i = row[1].replace(',', '')
    population_2015.append(int(i))
print(population_2015)

population_2025 = []
region_x = []
for row in data_2025[1:]:
    region = row[0].split(' ')[0]
    region_x.append(region)
    i = row[1].replace(',', '')
    population_2025.append(int(i))
print(population_2025)
print(region_x)

population_differences = [a - b for a, b in zip(population_2025, population_2015)]
print(population_differences)

#%%

import matplotlib.pyplot as plt

plt.rc('font', family ='Malgun Gothic') 
plt.xticks(rotation=90)
bar = plt.bar(region_x, population_differences)

for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', color='red', size = 8)

plt.savefig('savefig_Q4-1.png', bbox_inches='tight')
plt.show()
