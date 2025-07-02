# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:24:11 2025

@author: narae
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

mtcars = pd.read_csv("finaldata/mtcars.csv")

mtcars_hp = pd.DataFrame(mtcars.hp)

scaler=MinMaxScaler()
x=scaler.fit_transform(mtcars_hp)

count = 0
for i in range(len(x)):
    if x[i] > 0.7:
        count = count + 1

print(count)
