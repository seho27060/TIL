# 230125 1202 보석도둑
#  n <= 300,000

import sys
from heapq import *

input = sys.stdin.readline

n, k = map(int,input().split())
jewels = []
for _ in range(n):
    heappush(jewels,list(map(int,input().split())))

bags = [int(input()) for _ in range(k)]
bags.sort()

result = []
answer = 0

for idx in range(len(bags)):
    nowBag = bags[idx]

    while jewels and nowBag >= jewels[0][0]:
        heappush(result,-heappop(jewels)[1])
    if result:
        answer -= heappop(result)
    elif not jewels:
        break

print(answer)