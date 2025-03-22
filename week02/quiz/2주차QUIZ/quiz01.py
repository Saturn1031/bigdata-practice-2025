# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:57:22 2025

@author: DS
"""

def common_data(list1, list2):
    for i in list1:
        if i in list2:
            return True
    
    return None


print(common_data([1,2,3,4,5], [5,6,7,8,9]))    # -> True
print(common_data([1,2,3,4,5], [6,7,8,9]))      # -> None
