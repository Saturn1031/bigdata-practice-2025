# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 13:38:52 2025

@author: DS
"""

import os
import sys
import urllib.request
import datetime
import time
from bs4 import BeautifulSoup
import pandas as pd


# [CODE 1]
def getRequestUrl(url):    
    req = urllib.request.Request(url)
    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


responseDecode = getRequestUrl('https://www.weather.go.kr/weather/observation/currentweather.jsp')

soup = BeautifulSoup(responseDecode, 'html.parser')
table = soup('table')[0]

table_rows = table.find_all('tr')
table_headers = table_rows[:2]
table_data = table_rows[2:]
table_data_elements = [x.find_all('th') + x.find_all('td') for x in table_data]

data = []

for elem in table_data_elements:
    if len(elem) > 0:
        data.append([x.text for x in elem])
df = pd.DataFrame(data)

header_text0 = [x.text for x in table_headers[0].find_all('th')][1:]
header_text1 = [x.text for x in table_headers[1].find_all('th')][1:]
header = [header_text0[0].replace('\r\n\t\t', '')] + header_text1
df.columns = header

df_selected = df[['날씨', '현재기온', '습도%']].copy()
df_selected = df_selected.rename(columns={'날씨':'지역'})

print(df_selected)