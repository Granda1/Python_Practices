'''
(1).Human-like Artical Summarization
https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/

(2).Extractive Artical Summarization
https://tldrthis.p.rapidapi.com/v1/model/extractive/summarize-url/
 (1)과 (2)는 URL 형식으로 글을 입력받는다.

(3).Human-like Text Summarization
https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-text/

(4).Extractive Text Summarization
https://tldrthis.p.rapidapi.com/v1/model/extractive/summarize-text/
 (3)과 (4)는 텍스트 형식으로 글을 입력받는다.

Human-like는 기존 input text를 새롭게 re-phrasing한다.
Etractive는 input-text를 그대로 사용한다.

https://rapidapi.com/tldrthishq-tldrthishq-default/api/tldrthis/
위 URL로 들어가서 요약 형식을 바꾸면 된다.
'''


rapidapi_key = '40fe6185b1msh39671f6973c9c38p16fa17jsn5c8b65288c3e'
naver_client_id = 'H29aIvzvViVmUxv4eM9p'
naver_client_secret = 'LumkP6IZwD'

import requests
from pprint import pprint

url = 'https://tldrthis.p.rapidapi.com/v1/model/extractive/summarize-url/'

payload = {
    'url':'https://www.biblegateway.com/passage/?search=Genesis%201&version=NIV',
    'min_length': 100,
    'max_length': 300,
    'is_detailed': False
}

headers = {
    'content-type':'application/json',
    'X-RapidAPI-Key':'8f54fee791mshf855b5b32ffbbd0p1e668ejsn068f298d422a',
    'X-RapidAPI-Host':'tldrthis.p.rapidapi.com'
}

response = requests.request('POST',url,json=payload,headers=headers)

pprint(response.json())

# summary = response.json()['summary'][0].strip()
# print(summary)




# 여기에서 부터는 번역 부분이다.
# url = 'https://openapi.naver.com/v1/papago/n2mt'
#
# payload = {
#     'source':'en',
#     'target':'ko',
#     'text':summary,
# }
#
#
# headers = {
#     'content-type':'application/json',
#     'X-Naver-Client-Id':naver_client_id,
#     'X-Naver-Client-Secret':naver_client_secret,
# }
# response = requests.request('POST',url,json=payload,headers=headers)
# pprint(response.json())


