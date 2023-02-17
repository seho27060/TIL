# 230217 2293 동전 1

# n개 동전으로 k원을 만드는 경우의 수를 구하라

import sys

input = sys.stdin.readline

n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for won in range(coin,k+1):
        if won - coin >= 0:
            dp[won] += dp[won-coin]
            print(won,coin,dp)
print(dp[k])