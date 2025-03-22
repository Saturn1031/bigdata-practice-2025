# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 23:28:59 2025

@author: narae
"""

import csv
with open('emp.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    data_list = list(reader)

print(data_list)