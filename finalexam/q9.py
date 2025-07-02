# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:34:06 2025

@author: narae
"""

from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score

y_test = [0, 0, 0, 1, 1, 0, 1, 1, 0, 1]
y_prediction= [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]

confusion_matrix(y_test, y_prediction)
acccuracy = accuracy_score(y_test, y_prediction)
precision = precision_score(y_test, y_prediction)
recall = recall_score(y_test, y_prediction)

print('y_test = ', y_test)
print('y_prediction = ', y_prediction)
print(confusion_matrix(y_test, y_prediction))

print(acccuracy, precision, recall)
