import json

import naverMapCrawler
import pandas as pd

rawData = pd.read_csv("text.csv")

reviewData = []
try:
    reviewData = pd.read_csv("result.json")
except:
    print("결과 데이터 없음. 새로 생성")
rawDataList = rawData.drop("Unnamed: 0", axis = 1)
print(rawDataList.columns)

for idx in range(2):
    searchWord = ""
    rawData = rawDataList.loc[idx,["상호명","도로명주소"]]
    for word in rawData:
        searchWord += word + " "
    searchWord = searchWord.rstrip()
    print(searchWord)
    result = naverMapCrawler.crawler(searchWord)
    if result:
        reviewData.append(result)

print(reviewData)

# # json 파일로 저장
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(reviewData, f, indent=4, ensure_ascii=False)