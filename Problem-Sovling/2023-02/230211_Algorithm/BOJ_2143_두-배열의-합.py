# 230211 2143 두 배열의 합
# 한 개 배열 길이는 n < 1000.  n*n으로 시작 i 부터 끝 j까지 부분 역속배열 함 구하면..
# 1,000,000 이분탐색 **2

import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
n = int(input())
arrayA = list(map(int,input().split()))
m = int(input())
arrayB = list(map(int,input().split()))

sumDictA = defaultdict(int)
for start in range(n):
    for end in range(start+1,n+1):
        sumDictA[sum(arrayA[start:end])] += 1

sumDictB = defaultdict(int)
for start in range(m):
    for end in range(start+1,m+1):
        sumDictB[sum(arrayB[start:end])] += 1

sumListA = sorted(sumDictA.items(),key=lambda x:x[0],reverse=True)
sumListB = sorted(sumDictB.items(),key=lambda x:x[0])

answer = 0
# a부분연속배열에 b부분연속배열의 합 -> 무조건 두개 쌍임
aIdx, bIdx = 0,0
while aIdx < len(sumListA) and bIdx < len(sumListB):
    a, b = sumListA[aIdx],sumListB[bIdx]

    if a[0] + b[0] > t:
        aIdx += 1
    elif a[0] + b[0] == t:
        aIdx += 1
        answer += a[1]*b[1]
    else:
        bIdx += 1
print(answer)