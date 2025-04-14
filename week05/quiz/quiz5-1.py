# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:08:30 2025

@author: DS
"""

#%%
import csv
f = open('subwaytime_201803.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
next(data)
s_in_201803 = [0] * 24
s_out_201803 = [0] * 24
for row in data :
    row[4:] = map(int, row[4:]) 
    for i in range(24) :
        s_in_201803[i] += row[4 + i * 2] # 201803 시간대별 승차인원
        s_out_201803[i] += row[5 + i * 2] # 201803 시간대별 하차인원
        
    
#%%
import csv
f = open('subwaytime_202003.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
next(data)
s_in_202003 = [0] * 24
s_out_202003 = [0] * 24
for row in data :
    row[4:] = map(int, row[4:]) 
    for i in range(24) :
        s_in_202003[i] += row[4 + i * 2] # 202003 시간대별 승차인원
        s_out_202003[i] += row[5 + i * 2] # 202003 시간대별 하차인원


#%%
import csv
f = open('subwaytime_202503.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
next(data)
s_in_202503 = [0] * 24
s_out_202503 = [0] * 24
for row in data :
    row[4:] = map(int, row[4:]) 
    for i in range(24) :
        s_in_202503[i] += row[4 + i * 2] # 202503 시간대별 승차인원
        s_out_202503[i] += row[5 + i * 2] # 202503 시간대별 하차인원


#%%
import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')

plt.plot(s_in_201803, label = '201803승차')
plt.plot(s_out_201803, label = '201803하차')
plt.plot(s_in_202003, label = '202003승차')
plt.plot(s_out_202003, label = '202003하차')
plt.plot(s_in_202503, label = '202503승차')
plt.plot(s_out_202503, label = '202503하차')

plt.legend()
plt.xticks(range(24), range(4,28))

plt.savefig('savefig_Q5-1.png', bbox_inches='tight')
plt.show()