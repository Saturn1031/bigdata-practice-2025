# -*- coding: utf-8 -*-
"""
Created on Sat May 17 14:50:23 2025

@author: narae
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf

# 데이터 생성
data = {'x' : [59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70],
        'y' : [209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204]}
data = pd.DataFrame(data)

# statsmodels의 ols 사용
ols_model = smf.ols('y ~ x', data=data).fit()
ols_pred = ols_model.predict(pd.DataFrame({'x': [58]}))[0]

# 결과 출력
print(f"statsmodels ols 예측값       : {ols_pred:.3f}")

ols_summary = ols_model.summary()
print(ols_summary)
