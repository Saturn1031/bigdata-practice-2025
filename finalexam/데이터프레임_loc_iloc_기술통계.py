import numpy as np
import pandas as pd

#%%

# 데이터프레임 만들기 (인덱스, 컬럼)
df = pd.DataFrame([[89.2, 92.5, 'B'], 
                   [90.8, 92.8, 'A'], 
                   [89.9, 95.2, 'A'],
                   [89.9, 85.2, 'C'],
                   [89.9, 90.2, 'B']], 
    columns = ['중간고사', '기말고사', '성적'], 
    index = ['1반', '2반', '3반', '4반', '5반'])

df
#     중간고사  기말고사 성적
# 1반  89.2  92.5  B
# 2반  90.8  92.8  A
# 3반  89.9  95.2  A
# 4반  89.9  85.2  C
# 5반  89.9  90.2  B

#%%

# [인덱스][칼럼] 조회 안 됨
df['1반']['중간고사']    # KeyError: '1반'
type(df)


# 데이터프레임에서 시리즈 조회하기
df['중간고사']
# 1반    89.2
# 2반    90.8
# 3반    89.9
# 4반    89.9
# 5반    89.9
# Name: 중간고사, dtype: float64
type(df['중간고사'])    # pandas.core.series.Series

# 시리즈에서 범위 조회하기 (숫자 인덱스)
df['중간고사'][0:2]
# 1반    89.2
# 2반    90.8
# Name: 중간고사, dtype: float64
type(df['중간고사'][0]) # numpy.float64
type(df['중간고사'][0:2])   # pandas.core.series.Series

# 시리즈에서 범위 조회하기 (이름 인덱스)
df['중간고사']['1반':'2반']
# 1반    89.2
# 2반    90.8
# Name: 중간고사, dtype: float64
type(df['중간고사']['1반':'2반']) # pandas.core.series.Series

#%% 

# loc 사용하기

# 데이터 프레임에서 이름 인덱스로 시리즈 조회하기 (행을 시리즈로)
df.loc['1반']
# 중간고사    89.2
# 기말고사    92.5
# 성적         B
# Name: 1반, dtype: object
type(df.loc['1반'])  # pandas.core.series.Series

# 모든 행의 한 컬럼 조회하기 (열을 시리즈로)
df.loc[:, '중간고사']
# 1반    89.2
# 2반    90.8
# 3반    89.9
# 4반    89.9
# 5반    89.9
# Name: 중간고사, dtype: float64
type(df.loc[:, '중간고사']) # pandas.core.series.Series
type(df.loc[:, ['중간고사']])   # pandas.core.frame.DataFrame

# 여러 행의 한 컬럼 조회하기
df.loc['1반':'2반']['중간고사']
# 1반    89.2
# 2반    90.8
# Name: 중간고사, dtype: float64

# 데이터 하나 조회하기
df.loc['1반']['중간고사']    # 89.2
df.loc['1반', '중간고사']    # 89.2
type(df.loc['1반', '중간고사'])  # numpy.float64
df.loc['1반'][0]

#%%

# iloc 사용하기

# 데이터 프레임에서 숫자 인덱스로 시리즈 조회하기 (행을 시리즈로)
df.iloc[0]
# 중간고사    89.2
# 기말고사    92.5
# 성적         B
# Name: 1반, dtype: object
type(df.iloc[0])    # pandas.core.series.Series

# 데이터 하나 조회하기
df.iloc[0]['중간고사']
type(df.iloc[0]['중간고사'])    # numpy.float64

#%%

# loc로 조건식 조회하기

df.성적
# 1반    B
# 2반    A
# 3반    A
# 4반    C
# 5반    B
# Name: 성적, dtype: object

# 컬럼 조건에 맞는 행들 출력하기
df.loc[df.성적 == 'B']
#     중간고사  기말고사 성적
# 1반  89.2  92.5  B
# 5반  89.9  90.2  B
type(df.loc[df.성적 == 'B'])  # pandas.core.frame.DataFrame

# 컬럼 조건에 맞는 행이면 True
df.성적 == 'B'
# 1반     True
# 2반    False
# 3반    False
# 4반    False
# 5반     True
# Name: 성적, dtype: bool
type(df.성적)     # pandas.core.series.Series

# True 행들 출력하기
df.loc[[True, False, False, False, True]]
#     중간고사  기말고사 성적
# 1반  89.2  92.5  B
# 5반  89.9  90.2  B

# and 조건, 포함(isin) 조건
df.loc[(df.성적 == 'A') & (df.중간고사 >= 90)]
df.loc[df.성적.isin(['B', 'C'])]

#%%

# 데이터프레임 기술통계
df.describe()
#             중간고사      기말고사
# count   5.000000   5.00000    갯수
# mean   89.940000  91.18000    평균
# std     0.568331   3.78312    표준편차
# min    89.200000  85.20000    최솟값
# 25%    89.900000  90.20000    1사분위수
# 50%    89.900000  92.50000    중앙값
# 75%    89.900000  92.80000   	3사분위수
# max    90.800000  95.20000    	최댓값

# 시리즈 기술통계
df.중간고사.describe()
# count     5.000000
# mean     89.940000
# std       0.568331
# min      89.200000
# 25%      89.900000
# 50%      89.900000
# 75%      89.900000
# max      90.800000
# Name: 중간고사, dtype: float64

#%%

# 데이터프레임 위에서부터 한 행 출력
df.head(1)

# 시리즈에서 중복값 제거
df.중간고사.unique()    # array([89.2, 90.8, 89.9])

# 시리즈에서 평균값
df.중간고사.mean()

# 시리즈에서 종류별 갯수
df.중간고사.value_counts()
# 중간고사
# 89.9    3
# 89.2    1
# 90.8    1
# Name: count, dtype: int64

# 시리즈 각 값에 대한 계산
df_mean = df.중간고사.mean()
df.중간고사.map(lambda p: p - df_mean)
# 1반   -0.74
# 2반    0.86
# 3반   -0.04
# 4반   -0.04
# 5반   -0.04
# Name: 중간고사, dtype: float64

#%%

# 그룹과 정렬

# 중간고사 값이 같은 그룹에서 각 갯수
df.groupby('중간고사').중간고사.count()
# 중간고사
# 89.2    1
# 89.9    3
# 90.8    1
# Name: 중간고사, dtype: int64

# 중간고사 값이 같은 그룹에서 각 최솟값
df.groupby('중간고사').중간고사.min()
# 중간고사
# 89.2    89.2
# 89.9    89.9
# 90.8    90.8
# Name: 중간고사, dtype: float64

# 여러 개 통계 함수를 동시에 적용
df.groupby(['중간고사']).중간고사.agg([len, min, max])
#       len   min   max
# 중간고사                 
# 89.2    1  89.2  89.2
# 89.9    3  89.9  89.9
# 90.8    1  90.8  90.8

# 특정 컬럼 기준으로 정렬
df.sort_values(by='중간고사')   # 오름차순
df.sort_values(by='중간고사', ascending=False)  # 내림차순

# 인덱스 기준으로 정렬
df.sort_index(ascending=False)  # 내림차순

#%%

# 데이터 타입

# 컬럼별(시리즈별) 데이터 타입
df.dtypes
# 중간고사    float64
# 기말고사    float64
# 성적       object
# dtype: object
df.중간고사.dtypes   # dtype('float64')

# 행 삽입
df.loc['6반']=[10, 10, np.nan]

# 성적이 null인 행 찾기
df[pd.isnull(df.성적)]

#%%

# 시리즈, 인덱스 이름 수정

# 컬럼(시리즈) 이름 수정
df.rename(columns={'성적': '등급'})     # 성적 -> 등급

# 인덱스 이름 수정
df.rename_axis("반이름", axis='rows')
#       중간고사  기말고사   성적
# 반이름                 
# 1반   89.2  92.5    B
# 2반   90.8  92.8    A
# 3반   89.9  95.2    A
# 4반   89.9  85.2    C
# 5반   89.9  90.2    B
# 6반   10.0  10.0  NaN

#%%

# 데이터프레임 합치기

df1 = pd.DataFrame([[89.2, 92.5, 'B'], 
                   [90.8, 92.8, 'A'], 
                   [89.9, 95.2, 'A'],
                   [89.9, 85.2, 'C'],
                   [89.9, 90.2, 'B']], 
    columns = ['중간고사', '기말고사', '성적'], 
    index = ['1반', '2반', '3반', '4반', '5반'])

# 데이터프레임 2개 합치기
df0=pd.concat([df, df1])

# csv로 저장
df.to_csv('scores.csv',encoding='cp949')

# csv를 데이터프레임으로, 첫 번째 열을 인덱스로 사용
mydf = pd.read_csv('scores.csv', encoding='cp949', index_col=0, engine='python')

