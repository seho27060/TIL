#230313 12865 평범한 배낭
# 네 배낭하면 디피죠
# n <= 100 개의 물건읜 무게 w와 가치 v를 갖는다.
# 배낭은 k <= 100,000까지 버틸 수 있다.
# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력
import copy
import sys

input = sys.stdin.readline

n, k = map(int,input().split())

stuffs = []

for idx in range(n):
    weight, value = map(int,input().split())
    stuffs.append([weight,value])
    
napsack = [0 for _ in range(k+1)]

for stuff in stuffs:

    for weight in range(k,stuff[0]-1,-1):
        napsack[weight] = max(napsack[weight],napsack[weight-stuff[0]]+stuff[1])

print(max(napsack))