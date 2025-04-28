# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 13:15:11 2025

@author: DS
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

with open("중국_방한외래관광객_2020_202412.json", 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    
items = json_data

df = pd.DataFrame(items)

plt.figure()
plt.bar(df['yyyymm'], df['visit_cnt'])

plt.xlabel('yyyymm')
plt.ylabel('persons')
plt.title('Visitors')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()