# 230119 12015 가장 긴 증가하는 부분 수열 2
# 수열을 주고 가장 긴 증가하는 부분 수열을 구하라

# n <= 1,000,000
# On or O(nlogn)

# LIS를 사용하자! = DP + 이진탐색
# dp는 길이가 l인 부분 수열의 마지막 값

import sys

input = sys.stdin.readline

def binarySearch(lst,dpLen ,value):

    start, end = 0, dpLen -1

    while start <= end < dpLen:
        mid = (start + end)//2

        if lst[mid] < value:
            start = mid + 1
            if value <= lst[mid+1]:
                return mid+1
        else:
            end = mid -1
    return -1

n = int(input())
permu = list(map(int,input().split()))

dp = [-1]*(n+1)
dp[0] = 0
dpLen = 1
for idx in range(n):
    result = binarySearch(dp,dpLen,permu[idx])
    if result == -1:
        dp[dpLen] = permu[idx]
        dpLen += 1
    else:
        dp[result] = permu[idx]
print(dpLen - 1)

