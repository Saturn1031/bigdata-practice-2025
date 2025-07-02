# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:54:09 2025

@author: narae
"""

import numpy as np
import pandas as pd

emp = pd.read_csv('finaldata/emp.csv')

emp.groupby('deptno').sal.agg(['mean']).sort_values('mean', ascending=False)

