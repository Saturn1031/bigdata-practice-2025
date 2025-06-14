# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 22:46:33 2025

@author: narae
"""

import os
os.environ["PYTHONIOENCODING"] = "utf-8"

import pandas as pd
import re
nsmc_train_df = pd.read_csv('../DATA/ratings_train.txt', encoding='utf8', sep='\t', engine='python')
nsmc_train_df = nsmc_train_df[nsmc_train_df['document'].notnull()]
nsmc_train_df['document'] = nsmc_train_df['document'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', " ", x))

from konlpy.tag import Okt
okt = Okt()

def okt_tokenizer(text):
    tokens = okt.morphs(text)
    return tokens

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(tokenizer = okt_tokenizer, ngram_range=(1,2), min_df=3, max_df=0.9)
tfidf.fit(nsmc_train_df['document'])
nsmc_train_tfidf = tfidf.transform(nsmc_train_df['document'])

from sklearn.linear_model import LogisticRegression
SA_lr = LogisticRegression(random_state = 0)

from sklearn.model_selection import GridSearchCV
params = {'C': [1, 3, 3.5, 4, 4.5, 5]}
SA_lr_grid_cv = GridSearchCV(SA_lr, param_grid=params, cv=3, scoring='accuracy', verbose=1)
SA_lr_grid_cv.fit(nsmc_train_tfidf, nsmc_train_df['label'])
SA_lr_best = SA_lr_grid_cv.best_estimator_



st = input('감성 분석할 문장 입력 >> ')

#0) 입력 텍스트에 대한 전처리 수행
st = re.compile(r'[ㄱ-ㅣ가-힣]+').findall(st)
print(st)
st = [" ".join(st)]
print(st)

#1) 입력 텍스트의 피처 벡터화
st_tfidf = tfidf.transform(st)

#2) 최적 감성 분석 모델에 적용하여 감성 분석 평가
st_predict = SA_lr_best.predict(st_tfidf)

#3) 예측값 출력하기
if(st_predict == 0):
    print(st , "->> 부정 감성")
else :
    print(st , "->> 긍정 감성")