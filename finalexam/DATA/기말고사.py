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
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

# 인코딩 - 명목형 변수

# 스케일링

# 훈련/평가 데이터 분할 (7.5:2.5)

# 모델 학습

# 모델 성능 평가, accuracy 평가 점수 계산 print(accuracy)

# 테스트 데이터 예측

# 테스트 데이터 결과 제출
#submission_df = pd.DataFrame({'id': test.id, 'product_interest': test_preds})
#submission_df.to_csv("final_submission.csv", index=False)
