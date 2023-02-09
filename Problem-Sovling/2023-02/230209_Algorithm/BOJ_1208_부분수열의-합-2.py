# 230209 1208 부분수열의 합 2
# N < 40 짜리 수열에서
# 크기가 양수의 부분 수열 중
# 그 수열의 원소 합이 S인
# 경우의 수를 구하라
# 0~n//2, n//2 ~ n 배열로 나눠서
# 조합으로 합 구하기 -> 따로 빼놓음 -> 거기서 s인 값 카운팅 -> 딕셔너리로 {값:(경우의수1, 경우의수2)}
# 이제는 왼쪽배열의 경우의 수/ 오른쪽배열이 경우의 수 값으로 카운팅..
# 왼쪽 = {-1:(0,1),(1,2),0:(1),(2)} 오른쪽 = {0:(1,0),1:(3,2)}가 있을때,
# s=0인 값을 찾으면, 왼쪽에서 2개, 오른쪽에서 1개
# 왼쪽 -1 * 오른쪽 1 = 2*1 + 왼쪽 0 * 오른쪽 0 = 2*1
# 일케해서 구하기

import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline

n, s = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
leftNums = nums[:n//2].copy()
rightNums = nums[n//2:].copy()
answer = 0

dictForLeftCombinations = defaultdict(int)
for cnt in range(1,len(leftNums)+1):
    combis = list(combinations(leftNums,cnt))
    for com in combis:
        numSum = sum(com)
        if numSum == s:
            answer += 1
            # print(com)
        dictForLeftCombinations[numSum] += 1

dictForRightCombinations = defaultdict(int)
for cnt in range(1, len(rightNums)+1):
    combis = list(combinations(rightNums,cnt))
    for com in combis:
        numSum = sum(com)
        if numSum == s:
            answer += 1
            # print(com)
        dictForRightCombinations[numSum] += 1

leftNums = sorted(dictForLeftCombinations.keys())
rightNums = sorted(dictForRightCombinations.keys())
left,right = 0, len(rightNums)-1

while 0 <= left < len(leftNums) and 0 <= right < len(rightNums):
    result = leftNums[left] + rightNums[right]

    if result <= s:
        if result == s:
            answer += dictForLeftCombinations[leftNums[left]]*dictForRightCombinations[rightNums[right]]
        left += 1
    else:
        right -= 1
print(answer)