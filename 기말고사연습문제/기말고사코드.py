#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
X_train = pd.read_csv("XX_train.csv")
Y_train = pd.read_csv("YY_train.csv")
X_test = pd.read_csv("X_test.csv")
X_train.info()

# 인코딩
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
X_train["Warehouse_block"] = encoder.fit_transform(X_train["Warehouse_block"])
X_test["Warehouse_block"] = encoder.fit_transform(X_test["Warehouse_block"])
X_train["Mode_of_Shipment"] = encoder.fit_transform(X_train["Mode_of_Shipment"])
X_test["Mode_of_Shipment"] = encoder.fit_transform(X_test["Mode_of_Shipment"])
X_train["Product_importance"] = encoder.fit_transform(X_train["Product_importance"])
X_test["Product_importance"] = encoder.fit_transform(X_test["Product_importance"])
X_train["Gender"] = encoder.fit_transform(X_train["Gender"])
X_test["Gender"] = encoder.fit_transform(X_test["Gender"])

# train-test 검증 데이터 분리 20%
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)

# 모델 생성1(RandomForest)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=1000)
model.fit(X_train, y_train["Target"])

# # 모델 성능 평가
from sklearn.metrics import roc_auc_score
pred1 = model.predict(X_val)
acc = roc_auc_score(y_val["Target"], pred1) # 정확도
print(acc)

# 제출
pred = model.predict(X_test)
submit = pd.DataFrame({"ID": X_test["ID"], "Predicted": pred})
submit.to_csv("submission.csv", index=False)

