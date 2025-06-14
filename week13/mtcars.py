import pandas as pd
data=pd.read_csv("mtcars.csv")
print(data)

dir(pd) # 모듈 내 함수 목록
pd.read_csv.__doc__
print(pd.read_csv.__doc__)  # 함수 설명
print(pd.DataFrame.head.__doc__)

print(data.head())
print(data.shape)   # (열, 행)
print(type(data))
print(data.columns)
print(data.describe())  # 개수, 최소, 최대, 평균 등
print(data['hp'].describe())
print(data['gear'].unique())
print(data['cyl'].unique())

print(data.info())  # 컬럼 정보

print(data[["mpg", "cyl", "disp", "hp", 
            "drat", "wt", "qsec", "vs", 
            "carb"]].corr())
X=data.drop(columns='mpg')
Y=data['mpg']
