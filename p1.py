
#%%
# #$$ shift+enter
print('hello world')
# %%
# 변수명명규칙
1=1
print(a1)

# %%
# 리스트
a=[1,'1',[2,3,'사']]
print(a,'타입:', type(a), type(a[0]), type(a[1]))
a[0]=5 # 수정가능하다
print(a)

# %%
# 튜플 
a=(1,'1',[2,3,'사'])
print(a,'타입:', type(a), type(a[0]), type(a[1]))
a[0]=5 # 수정불가 = 
print(a)
# 리스트와 튜플의 차이점은 수정 가능 & 불가능

# %%
# 딕셔너리
b={'한국':'서울','일본':'도쿄'}
print(b, type(b), b['한국']) # 접근은 키값을 넣어서 접근

# %%
# 집합 - 중복방지
c=set([1,1,2,3,4,5])
print(c,type(c))

# %%
import numpy as np
# 동일데이터 타입으로 변환하여 사용
a = [1,2,3,'4']
ar=np.array(a).astype(int)
print(ar,type(ar))

# %%
# 자유로운 동일한 형변환
#  a=range(10)
# print(a,type(a),ar,type((ar))
# for i in range(10):
#     print(i)

# %%
# 형태변환(차원변환)이 자유로움
print(ar, '형태:',ar.shape)
ar34=ar.reshape(3,4)
print(ar34,'차원:',ar34.shape)

# %%
# 슬라이싱
ar34[1:,1:]

# %%
