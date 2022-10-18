import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm, tqdm_pandas

model = SentenceTransformer('jhgan/ko-sroberta-multitask')

# 아래 세줄은 한국어 임베딩을 설명하는 코드이다.
'''
# sentences = ['안녕하세요?','한국어 문장 임베딩을 위한 버트 모델입니다.']
# embedding = model.encode(sentences)
# print(embedding)
'''

# 아래 다섯 줄은 상담 데이터셋을 챗봇에 쓸 수 있게 바꾸고 저장하는 과정이다.
'''
# df = pd.read_csv('C:/Users/Daniel Hanjoo Rhee/PycharmProjects/Practice/Chat_Bot/wellness_dataset_original.csv')
# df = df.drop(columns=['Unnamed: 3'])
# df = df[~df['챗봇'].isna()]
# df['embedding'] = pd.Series([[]] * len(df))
# df['embedding'] = df['유저'].map(lambda x: list(model.encode(x)))
# df.to_csv('C:/Users/Daniel Hanjoo Rhee/PycharmProjects/Practice/Chat_Bot/wellness_dataset.csv',index=False)
'''

df = pd.read_csv('C:/Users/Daniel Hanjoo Rhee/PycharmProjects/Practice/Chat_Bot/wellness_dataset_original.csv')
df = df.drop(columns=['Unnamed: 3'])
df = df[~df['챗봇'].isna()]
df['embedding'] = pd.Series([[]] * len(df))
df['embedding'] = df['유저'].map(lambda x: list(model.encode(x)))


# 일단 위에서 작업하여 만든 데이터셋을 다시 불러왔다.
# df1 = pd.read_csv('C:/Users/Daniel Hanjoo Rhee/PycharmProjects/Practice/Chat_Bot/wellness_dataset.csv')
# print(df1.head())

text = input('당신의 상담 받고자 하는 내용을 입력해주세요.: ')
embedding = model.encode(text)
df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())



answer = df.loc[df['distance'].idxmax()]

# print('구분', answer['구분'])
# print('유사한 질문', answer['유저'])
print('챗봇 답변', answer['챗봇'])
# print('유사도', answer['distance'])