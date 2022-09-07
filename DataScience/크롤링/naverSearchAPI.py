import json
import os
import sys
import urllib.request

import pandas as pd

# 2만 5천건 실행.

client_id = "PnGoJDVEfbKBxWTZxz3H"
client_secret = "FCdMYW54NT"

# testData = pd.read_csv("C:/Users/seho2/Desktop/크롤링/text.csv")
#
# print(testData.columns)
# print(testData.shape)
# print(testData.describe())
#
# for data in testData["상호명"][:10]:
#     print(data)

encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&start=1&sort=sim" # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

getURLlst = []
if(rescode==200):
    response_body = json.load(response)
    for getBody in response_body["items"]:
        getURLlst.append(getBody["link"])
    # response_body = response.read()
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

print(len(getURLlst),"url 개수")
for kk in getURLlst:
    print(kk)
# 상호명 검색에 대한 블로그 url 수집.