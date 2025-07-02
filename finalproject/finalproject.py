# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:57:27 2025

@author: narae
"""

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from matplotlib import cm
from sklearn.metrics import silhouette_samples

def clusterScatter(n_cluster, X_features): 
    X_features = X_features.values if isinstance(X_features, pd.DataFrame) else X_features
    
    c_colors = []
    kmeans = KMeans(n_clusters=n_cluster, random_state=0)
    Y_labels = kmeans.fit_predict(X_features)

    for i in range(n_cluster):
        c_color = cm.jet(float(i) / n_cluster) #클러스터의 색상 설정
        c_colors.append(c_color)
        #클러스터의 데이터 분포를 동그라미로 시각화
        plt.scatter(X_features[Y_labels == i,0], X_features[Y_labels == i,1],
                     marker='o', color=c_color, edgecolor='black', s=50, 
                     label='cluster '+ str(i))       
    
    #각 클러스터의 중심점을 삼각형으로 표시
    for i in range(n_cluster):
        plt.scatter(kmeans.cluster_centers_[i,0], kmeans.cluster_centers_[i,1], 
                    marker='^', color=c_colors[i], edgecolor='w', s=200)
        
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def silhouetteViz(n_cluster, X_features): 
    
    kmeans = KMeans(n_clusters=n_cluster, random_state=0)
    Y_labels = kmeans.fit_predict(X_features)
    
    silhouette_values = silhouette_samples(X_features, Y_labels, metric='euclidean')

    y_ax_lower, y_ax_upper = 0, 0
    y_ticks = []

    for c in range(n_cluster):
        c_silhouettes = silhouette_values[Y_labels == c]
        c_silhouettes.sort()
        y_ax_upper += len(c_silhouettes)
        color = cm.jet(float(c) / n_cluster)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouettes,
                 height=1.0, edgecolor='none', color=color)
        y_ticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouettes)
    
    silhouette_avg = np.mean(silhouette_values)
    plt.axvline(silhouette_avg, color='red', linestyle='--')
    plt.title('Number of Cluster : '+ str(n_cluster)+'\n'               + 'Silhouette Score : '+ str(round(silhouette_avg,3)))
    plt.yticks(y_ticks, range(n_cluster))   
    plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient')
    plt.tight_layout()
    plt.show()


crime_by_region = pd.read_csv('data/경찰청_범죄 발생 지역별 통계_20231231.csv', encoding='cp949')

visa_by_region = pd.read_csv('data/시군구별 및 체류자격별 등록외국인 현황.csv', encoding='cp949')
visa_by_region = visa_by_region.rename(columns={"행정구역(시군구)별": "행정구역별"})
visa_by_region = visa_by_region.rename(columns={"2023 년": "외국인인구"})
visa_by_region.행정구역별 = visa_by_region.행정구역별.str.split(' ').str.get(0)

population_by_region = pd.read_csv('data/지역별(행정동) 성별 연령별 주민등록 인구수_20231231.csv', encoding='cp949')
population_by_region.시군구명 = population_by_region.시군구명.str.split(' ').str.get(0)
population_by_region.시도명.replace('전라북도', '전북특별자치도', inplace=True)
population_by_region = pd.DataFrame(population_by_region.groupby(['시도명', '시군구명'], dropna=False, as_index=False).계.sum())

regions = ['강원특별자치도', '경기도', '경상남도', '경상북도', '광주광역시', 
           '대구광역시', '대전광역시', '부산광역시', '서울특별시', '세종특별자치시', 
           '울산광역시', '인천광역시', '전라남도', '전북특별자치도', 
           '제주특별자치도', '충청남도', '충청북도']

regions_short = ['강원도', '경기도', '경남', '경북', '광주', 
                 '대구', '대전', '부산', '서울', '세종시', 
                 '울산', '인천', '전남', '전북', 
                 '제주', '충남', '충북']


#%%

# 도시별 외국인 거주자 수와 범죄율의 상관관계 (선형회귀)

foreigner_by_region = visa_by_region[(visa_by_region.체류자격별 == '총계') 
                                     & (visa_by_region.성별 == '계')
                                     & (visa_by_region.행정구역별 != '총계')]

crime_rate = []
foreigner_rate = []

for i in range(len(foreigner_by_region)):
    if (foreigner_by_region.iloc[i].행정구역별 in regions) \
        and (not foreigner_by_region.iloc[i].행정구역별 == '세종특별자치시'):
        city = foreigner_by_region.iloc[i].행정구역별 
        index = regions.index(foreigner_by_region.iloc[i].행정구역별)
        city_short = regions_short[index]
        continue
    
    if foreigner_by_region.iloc[i].행정구역별 == '세종특별자치시':
        city = foreigner_by_region.iloc[i].행정구역별
        index = regions.index(foreigner_by_region.iloc[i].행정구역별)
        city_short = regions_short[index]
        region = city_short
         
    else: 
        region = city_short + foreigner_by_region.iloc[i].행정구역별
        
    crime_count = crime_by_region[region].sum()
    population = population_by_region[
        (population_by_region.시도명 == city) & 
        (
            (population_by_region.시군구명 == foreigner_by_region.iloc[i].행정구역별) | 
            (population_by_region.시군구명.isna())
        )
    ].계.sum()
    foreigner_population = foreigner_by_region.iloc[i].외국인인구.sum()
    
    crime_rate.append(crime_count / population)
    foreigner_rate.append(foreigner_population / population)
    
    print(region + ': ', crime_rate[-1])
    


olsDic = {
    'crime_rate': np.array(crime_rate),
    'foreigner_rate': np.array(foreigner_rate)
    }
crimeRateDf = pd.DataFrame(olsDic)

ols_model = smf.ols('crime_rate ~ foreigner_rate', crimeRateDf).fit()
ols_summary = ols_model.summary()
print(ols_summary)

sns.regplot(x='foreigner_rate', y='crime_rate', data=crimeRateDf)
plt.savefig('외국인거주율_범죄율_선형회귀.png', bbox_inches='tight')
plt.show()

# 상관 계수
crimeRateDf_corr = crimeRateDf.corr(method = 'pearson')
crimeRateDf_corr.to_csv('외국인거주율_범죄율_상관계수.csv', index = False)


#%%

# 외국인 비자별 지역 클러스터링

foreigner_by_visa_region = visa_by_region[(visa_by_region.체류자격별 != '총계') 
                                     & (visa_by_region.성별 == '계')
                                     & (visa_by_region.행정구역별 != '총계')]

visaDf = pd.DataFrame()

for i in range(len(foreigner_by_visa_region)):
    
    if (foreigner_by_visa_region.iloc[i].행정구역별 in regions) \
        and (not foreigner_by_visa_region.iloc[i].행정구역별 == '세종특별자치시'):
        city = foreigner_by_visa_region.iloc[i].행정구역별 
        index = regions.index(foreigner_by_visa_region.iloc[i].행정구역별)
        city_short = regions_short[index]
        continue
    
    if foreigner_by_visa_region.iloc[i].행정구역별 == '세종특별자치시':
        city = foreigner_by_visa_region.iloc[i].행정구역별
        index = regions.index(foreigner_by_visa_region.iloc[i].행정구역별)
        city_short = regions_short[index]
        region = city_short
         
    else: 
        region = city_short + foreigner_by_visa_region.iloc[i].행정구역별
        
    visa_type = foreigner_by_visa_region.iloc[i].체류자격별
    if visa_type not in visaDf.columns:
        visaDf[visa_type] = pd.Series()
    visaDf.loc[region, visa_type] = foreigner_by_visa_region.iloc[i].외국인인구.sum()
    
    crime_count = crime_by_region[region].sum()
    population = population_by_region[
        (population_by_region.시도명 == city) & 
        (
            (population_by_region.시군구명 == foreigner_by_visa_region.iloc[i].행정구역별) | 
            (population_by_region.시군구명.isna())
        )
    ].계.sum()
    foreigner_population = foreigner_by_visa_region.iloc[i].외국인인구.sum()
    
    if 'crime_rate' not in visaDf.columns:
        visaDf['crime_rate'] = np.nan
    visaDf.loc[region, 'crime_rate'] = crime_count / population
        
    if 'foreigner_rate' not in visaDf.columns:
        visaDf['foreigner_rate'] = np.nan
    
    if pd.isna(visaDf.loc[region, 'foreigner_rate']):
        visaDf.loc[region, 'foreigner_rate'] = 0
    visaDf.loc[region, 'foreigner_rate'] = visaDf.loc[region, 'foreigner_rate'] + foreigner_population / population
    
   
for col in visaDf.columns:
    visaDf[col] = pd.to_numeric(visaDf[col], errors='coerce')

distortions = []
for i in range(1, 11):
    kmeans_i = KMeans(n_clusters=i, random_state=0)  # 모델 생성
    kmeans_i.fit(visaDf)   # 모델 훈련
    distortions.append(kmeans_i.inertia_)
    
plt.plot(range(1,11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0).fit(visaDf)


silhouetteViz(2, visaDf) #클러스터 2개인 경우의 실루엣 score 및 각 클러스터 비중 시각화
silhouetteViz(3, visaDf)
silhouetteViz(4, visaDf)
silhouetteViz(5, visaDf)
silhouetteViz(6, visaDf)
silhouetteViz(7, visaDf)
silhouetteViz(8, visaDf)

clusterScatter(2, visaDf) #클러스터 2개인 경우의 클러스터 데이터 분포 시각화
clusterScatter(3, visaDf)
clusterScatter(4, visaDf)
clusterScatter(5, visaDf)
clusterScatter(6, visaDf)
clusterScatter(7, visaDf)
clusterScatter(8, visaDf)


best_cluster = 3

kmeans = KMeans(n_clusters=best_cluster, random_state=0)
Y_labels = kmeans.fit_predict(visaDf)

visaDf['ClusterLabel'] = Y_labels

visaDfmean = visaDf.groupby('ClusterLabel').mean()

# 클러스터별 특징
visaDfmean.foreigner_rate
visaDfmean['비전문취업(E-9)']
visaDfmean['유학(D-2)']
visa_cluster_df = visaDfmean[['foreigner_rate', '비전문취업(E-9)', '유학(D-2)']]
visa_cluster_df

visaDf.groupby('ClusterLabel')['crime_rate'].count()

# 클러스터별 범죄율
visaDfmean.crime_rate


#%%

# 외국인 비자별 범죄율 상관관계 분석 (선형회귀)

rename_dict = {
    "문화예술(D-1)": "art_D1",
    "유학(D-2)": "study_D2",
    "기술연수(D-3)": "training_D3",
    "일반연수(D-4)": "training_D4",
    "취재(D-5)": "press_D5",
    "종교(D-6)": "religion_D6",
    "주재(D-7)": "reside_D7",
    "기업투자(D-8)": "invest_D8",
    "무역경영(D-9)": "trade_D9",
    "구직(D-10)": "jobseek_D10",
    "교수(E-1)": "prof_E1",
    "회화강사(E-2)": "instructor_E2",
    "연구(E-3)": "research_E3",
    "기술지도(E-4)": "tech_E4",
    "전문직업(E-5)": "projob_E5",
    "예술흥행(E-6)": "performance_E6",
    "특정활동(E-7)": "activity_E7",
    "계절근로(E-8)": "seasonal_E8",
    "비전문취업(E-9)": "nonprojob_E9",
    "선원취업(E-10)": "sailor_E10",
    "방문동거(F-1)": "visit_F1",
    "거주(F-2)": "reside_F2",
    "동반(F-3)": "accompany_F3",
    "영주(F-5)": "permanent_F5",
    "결혼이민(F-6)": "marriage_F6",
    "기타(G-1)": "etc_G1",
    "관광취업(H-1)": "tourism_H1",
    "방문취업(H-2)": "visitwork_H2",
    "기타(Others)": "etc_others"
}

visaDf = visaDf.rename(columns=rename_dict)

Rformula = '''crime_rate ~ foreigner_rate + art_D1 + study_D2 + training_D3 + 
training_D4 + press_D5 + religion_D6 + reside_D7 + invest_D8 + trade_D9 + jobseek_D10 + 
prof_E1 + instructor_E2 + research_E3 + tech_E4 + projob_E5 + performance_E6 + 
activity_E7 + seasonal_E8 + nonprojob_E9 + sailor_E10 + visit_F1 + reside_F2 + 
accompany_F3 + permanent_F5 + marriage_F6 + etc_G1 + tourism_H1 + visitwork_H2 + 
etc_others'''

visaDf.sum()

regression_result = smf.ols(Rformula, data = visaDf).fit()
regression_result.summary()

sns.regplot(x='sailor_E10', y='crime_rate', data=visaDf)
plt.show()

# 상관 계수
visaDf_corr = visaDf.corr(method = 'pearson')
visaDf_corr.to_csv('비자별_범죄율_상관계수.csv', index = True)
