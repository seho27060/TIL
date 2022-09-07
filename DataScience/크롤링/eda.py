import pandas as pd

csv_test = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_서울_202203.csv")

print(csv_test[:10])
print(csv_test.columns)
print(csv_test.shape)
# print(csv_test[csv_test["상권업종대분류명"] == "음식"].shape)
# # print()
# names = csv_test[csv_test["상권업종대분류명"] == "음식"]
# names.to_csv("text.csv")
# print(names)
# f = open('textUrls.txt', "w")

# for name in names[:10]:
#     print(name)
