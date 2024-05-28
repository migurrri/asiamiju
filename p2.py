#%%
# EDA
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
!pip install scikit-learn
# %%
import sklearn
print(sklearn.__version__)

# %%
from sklearn.datasets import load_iris
iris=load_iris()
print(type(iris), iris)

# %%
iris.keys()

# %%
print(iris['data'].shape)
# %%
df = pd.DataFrame(iris['data'])
df
# %%
print(iris['feature_names'])
# %%
cols = ['sl', 'sw', 'pl', 'pw']
df=pd.DataFrame(iris['data'], columns=cols)
df
# %%
cap = {'한국':'서울', '일본':'도쿄'}
print(type(cap), cap.keys(), cap.values())
# %%
print(iris['target'].shape)
# %%
print(iris['target_names'])
# %%
iris.keys()
print(iris['DESCR'])
# %%
# 대표값을 통한 EDA
df.describe()
# %%
# csv로 출력
df.to_csv('../pybasic/iris.csv')
# %%
plt.plot(df)
# %%
df.plot(kind="line")
# %%
df.plot(kind="kde")
# %%
df.plot(kind="scatter", x='sl', y='sw')
# %%
df.plot(kind="box")
# %%
!pip install seaborn
import seaborn as sns
sns.boxplot(df)
# %%
df
# %%
df['label'] = iris['target']
df
# %%
sns.pairplot(df)
# %%
sns.pairplot(df, hue='label')
# %%
df.values()
# %%
# 형태보기
df.shape()
# %%
# 기초통계자료
df.describe()
# %%
df.dtypes
# %%
df.head()
# %%
df.tail()
# 보시는 바와 같이 라벨이 반복되고 있어서 데이터의 순서적 편향이 존재
# 따라서 머신러닝의 경우 셔플하는 것이 필요할 것으로 확인된다
# %%
df = df.drop_duplicates()
df.shape
# %%
df.isna().sum()
df.dropna()
# 빈값은 없음
# %%
# 시각화
df['sl'].plot(kind = "hist", bins=10)
# 크게 정규성이 없어 보인다.

# %%
df.plot(kind = "scatter", x='sl', y='sw')
# %%
sns.pairplot(df,hue='label')
# 시각적으로 어느정도 분리될 것으로 보여지나
# 겹치는 부분이 많아서 통계적 분리는 어려울 것으로 보여진다.
# 우상향 하는 그래프로 볼때 상관성 분석이 필요할것으로 보인다.
# %%

sns.heatmap(df.iloc[:,0:4].corr(),annot=True)
# pw와 pl의 상관성이...

# %%
