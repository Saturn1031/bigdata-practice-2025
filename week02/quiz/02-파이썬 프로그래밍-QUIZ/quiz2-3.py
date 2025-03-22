# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 23:33:23 2025

@author: narae
"""

import pandas as pd
emp=pd.read_csv('emp.csv')

emp.head()
emp["ENAME"]
emp[emp["SAL"] > 2000]