# ### 1. 경제 기사 데이터를 마침표가 있는 문장별로 분리

import os
print(os.getcwd())


os.chdir("/Users/heosangbeom/Desktop/data_final")
os.getcwd()

import sys
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
df = pd.read_csv("total_articles_100.csv", encoding='cp949', )
df.head(10)


content = df[["content_new"]]
content.head()

df['split'] = df.content_new.str.split('.').str[0]
df['split']


# ### 2. 문장에서 동시 출현 빈도가 5번째로 높은 단어 토큰 쌍을 찾자
# #### 2-1. 단어 토큰은 okt 형태소 분석기 함수인 nouns()로 얻어진 단어 토큰을 이용한다.


from konlpy.tag import Okt 
okt = Okt()


text = "30일 아시아 증시는 오전장에서 혼조세가 뚜렷하다"
print(okt.nouns(text))

# dataframe을 list로 변환 후 텍스트화
text_list = np.array(df['split'].tolist())
text_list
text = ",".join(text_list)

#단어 단위로 토큰화
nouns = okt.nouns(text)
print(nouns)

from collections import Counter
from konlpy.tag import Twitter
import pytagcloud

count = Counter(nouns)
count.most_common(10)

# ## 따라서, 5번째로 높은 순서를 가지고 있는 단어는 "경제"이다.




