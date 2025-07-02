# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:42:52 2025

@author: narae
"""

import numpy as np
import pandas as pd

smoke = pd.read_csv("finaldata/smoke.csv")

smoke.count

per = 1070 * 15 / 100

male = smoke[smoke.sex=='male'].sort_values('bmi', ascending=False).head(160).charges.mean()
female = smoke[smoke.sex=='female'].sort_values('bmi', ascending=False).head(160).charges.mean()

print(male - female)
