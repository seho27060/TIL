from urllib.request import  urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
import pandas as pd
# html = urlopen('https://search.naver.com/search.naver?query='+str("숙성도"))
# bs = BeautifulSoup(html.read(), "html.parser")

testLst = pd.read_csv("text.csv")
print(testLst.shape)
print(testLst.head())

for name in testLst["상호명"][:10]:
    print(name)