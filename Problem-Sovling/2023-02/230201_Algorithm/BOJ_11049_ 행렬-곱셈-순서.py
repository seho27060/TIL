# 230201 11049 행렬 곱셈 순서

import sys

input = sys.stdin.readline

n = int(input())

matrices = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n) for _ in range(n)]

for i in range(1,n):
    for j in range(0,n-i):

        if i == 1:
            dp[j][j+i] = matrices[j][0]*matrices[j][1]*matrices[j+i][1]
        else:
            dp[j][j+i] = sys.maxsize
            for k in range(j,j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + matrices[j][0]*matrices[k][1]*matrices[j+i][1])
print(dp[0][-1])