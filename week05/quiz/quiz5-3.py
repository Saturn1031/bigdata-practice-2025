# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:03:53 2025

@author: DS
"""

#%%
import numpy as np
import csv
import pandas as pd

#1. 데이터를 읽어온다.
df = pd.read_csv('age.csv', encoding='cp949')
#2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
#3. 궁금한 지역의 인구 구조를 저장한다.

home_df = df[df.행정구역.str.contains(name)].iloc[:, 3:]
hometotal_df = int(df[df.행정구역.str.contains(name)]['총인구수'].iloc[0])
for k in range(home_df.shape[1]):
    home.append(int(home_df.iloc[:, k])/hometotal_df)
    
#4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
result_list=[]
for row in range(len(df)):
    away=[]
    away_df = df.iloc[row, 3:]
    awaytotal_df = int(df.iloc[row, :]['총인구수'])
    for k in range(len(away_df)):
        away.append(int(away_df.iloc[k])/awaytotal_df)
    s=0
    for j in range(len(away)):
        s=s+(home[j]-away[j])**2
    result_list.append([df.iloc[row, :]['행정구역'], away, s])
result_list.sort(key=lambda s: s[2]) # sum 값으로 정렬...

#5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)            
plt.rc('font', family ='Malgun Gothic')
plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
plt.plot(result_list[1][1], label = result_list[1][0])
plt.plot(result_list[2][1], label = result_list[2][0])
plt.plot(result_list[3][1], label = result_list[3][0])
plt.plot(result_list[4][1], label = result_list[4][0])
plt.plot(result_list[5][1], label = result_list[5][0])
plt.legend()

plt.savefig('savefig_Q5-3.png', bbox_inches='tight')
plt.show()
