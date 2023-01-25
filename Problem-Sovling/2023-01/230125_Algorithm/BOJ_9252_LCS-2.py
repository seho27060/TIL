# 230125 9252 LCS 2
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# 두 수열의 모두의 부분 수열이 되는 수열 중 가장 긴 것 찾기

import sys

input = sys.stdin.readline

aStr = list(input().rstrip())
bStr = list(input().rstrip())

result = [[0]*(len(bStr)+1) for _ in range(len(aStr)+1)]

for aIdx in range(1,len(aStr)+1):
    for bIdx in range(1,len(bStr)+1):
        if aStr[aIdx-1] == bStr[bIdx-1]:
            result[aIdx][bIdx] = result[aIdx-1][bIdx-1] + 1
        else:
            result[aIdx][bIdx] = max(result[aIdx-1][bIdx],result[aIdx][bIdx-1])

maxLen = result[-1][-1]
print(maxLen)
answer = []
bIdx = len(bStr)
aIdx = len(aStr)
while bIdx > 0 and aIdx > 0:
    if result[aIdx][bIdx-1] == result[aIdx][bIdx]:
        bIdx -= 1
    elif result[aIdx-1][bIdx] == result[aIdx][bIdx]:
        aIdx -= 1
    else:
        answer.append(aStr[aIdx-1])
        aIdx -= 1
        bIdx -= 1
answer.reverse()
print("".join(answer))