# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:51:11 2025

@author: narae
"""

#%%

import pandas as pd

data_2015 = pd.read_csv("201502_201502_주민등록인구및세대현황_월간.csv", encoding='cp949')
data_2025 = pd.read_csv("202502_202502_주민등록인구및세대현황_월간.csv", encoding='cp949')

population_2015 = data_2015['2015년02월_총인구수'].str.replace(',', '', regex=False).astype(int)
population_2025 = data_2025['2025년02월_총인구수'].str.replace(',', '', regex=False).astype(int)

region_x = data_2025['행정구역'].apply(lambda x: x.split(' ')[0])

population_differences = [a - b for a, b in zip(population_2025, population_2015)]

#%%

import matplotlib.pyplot as plt

plt.rc('font', family ='Malgun Gothic') 
plt.xticks(rotation=90)
bar = plt.bar(region_x, population_differences)

for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', color='red', size = 8)

plt.savefig('savefig_Q4-2.png', bbox_inches='tight')
plt.show()