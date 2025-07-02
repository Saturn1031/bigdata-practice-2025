# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:31:20 2025

@author: DS
"""

import pandas as pd

#%%

data = {
        'apples': [3, 2, 0, 1],
        'oranges': [0, 3, 7, 2]
}

# 딕셔너리로 데이터프레임 만들기
purchases = pd.DataFrame(data)
purchases
#    apples  oranges
# 0       3        0
# 1       2        3
# 2       0        7
# 3       1        2

purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
purchases
#         apples  oranges
# June         3        0
# Robert       2        3
# Lily         0        7
# David        1        2

#%%

# 리스트로 시리즈 만들기
col1=pd.Series([3, 2, 0, 1], name='apples')
col2=pd.Series([3, 2, 0, 1], name='oranges', index=['June', 'Robert', 'Lily', 'David'])
col2=pd.Series([3, 2, 0, 1], name='oranges')

col1
# 0    3
# 1    2
# 2    0
# 3    1
# Name: apples, dtype: int64
col1.name
col1.values
col1.index


# 1개의 시리즈로 데이터프레임 만들기
purchases2 = pd.DataFrame(col1)
purchases2
purchases3 = pd.DataFrame(col2)
purchases3


# 여러 개의 시리즈로 데이터프레임 만들기
purchases4= pd.concat([col1, col2], axis=1)
purchases4
#    apples  oranges
# 0       3        3
# 1       2        2
# 2       0        0
# 3       1        1


# 데이터프레임의 인덱스 수정하기
purchases4.index=['June', 'Robert', 'Lily', 'David']
purchases4
#         apples  oranges
# June         3        3
# Robert       2        2
# Lily         0        0
# David        1        1


purchases4.name
purchases4.index
purchases4.columns
