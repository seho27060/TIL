#230307 2631 줄세우기
# n <= 200 의 수로 순서를 의미하는 숫자들이 무작위로 입력된다.
# 최소의 횟수로 순서대로 정렬하는 옮기는 경우의 수를 구하라.

import sys

input = sys.stdin.readline

n = int(input())

kids = [int(input()) for _ in range(n)]

dp = [1]*(n)
for now in range(n):
    for comp in range(now):
        if kids[now] > kids[comp]:
            dp[now] = max(dp[now],dp[comp]+1)
print(n-max(dp))