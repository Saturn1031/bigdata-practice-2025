# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 22:02:56 2025

@author: USER
"""

# 코드 실행 상태가 초기화되었으므로 다시 필요한 파일을 복원 후 작업을 반복
import pandas as pd
import numpy as np
# import 문 필요

# 데이터 
X_train=pd.read_csv("train.csv")
Y_train=pd.DataFrame(X_train.product_interest)
X_train = X_train.drop(columns=['product_interest'])
test=pd.read_csv("test.csv")
X_test = test.drop(columns=['id'])

# 인코딩 - 명목형 변수
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
X_train["gender"] = encoder.fit_transform(X_train["gender"])
X_test["gender"] = encoder.fit_transform(X_test["gender"])
X_train["region"] = encoder.fit_transform(X_train["region"])
X_test["region"] = encoder.fit_transform(X_test["region"])


# 스케일링
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x=scaler.fit_transform(X_train)
X_train=pd.DataFrame(x, columns=X_train.columns)
x=scaler.transform(X_test)
X_test=pd.DataFrame(x, columns=X_test.columns)

# 훈련/평가 데이터 분할 (7.5:2.5)
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, Y_train, test_size=0.25, random_state=700)


# 모델 학습
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train['product_interest'])

# 모델 성능 평가, accuracy 평가 점수 계산 print(accuracy)
from sklearn.metrics import accuracy_score
y_prediction = model.predict(X_val)
acccuracy = accuracy_score(y_val, y_prediction)
print(acccuracy)

# 테스트 데이터 예측
Y_test = model.predict(X_test)

# 테스트 데이터 결과 제출
submission_df = pd.DataFrame({'id': test.id, 'product_interest': Y_test})
submission_df.to_csv("final_submission.csv", index=False)
