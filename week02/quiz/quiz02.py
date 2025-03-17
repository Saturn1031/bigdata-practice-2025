# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:05:47 2025

@author: DS
"""

def test(list, str):
    for i in list:
        if i in str:
            return True
    
    return False

str1 = "https://www.w3resource.com/python-exercises/list/"
lst = ['.com', '.edu', '.tv']
print(test(lst, str1))   # -> True

str1 = "https://www.w3resource.net"
lst = ['.com', '.edu', '.tv']
print(test(lst, str1))   # -> False