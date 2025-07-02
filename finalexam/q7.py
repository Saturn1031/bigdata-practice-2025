# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 11:54:17 2025

@author: narae
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train = pd.read_csv("finaldata/X.csv")
Y_train = pd.read_csv("finaldata/y.csv")

X_train.info()

X_train, X_val, y_train, y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)

model=LogisticRegression(max_iter=1000)
model.fit(X_train, y_train["target"])

pred1 = model.predict(X_val)
acccuracy = accuracy_score(y_val["target"], pred1)
print(acccuracy)
