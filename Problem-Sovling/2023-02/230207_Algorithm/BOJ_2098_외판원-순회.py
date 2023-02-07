# 230203 2098 외판원 순회
# dfs + dp + 비트마스킹의 콜라보레이션
import sys

input = sys.stdin.readline

def dfs(now,visited):
    global n, graphs, dp

    if visited == (1 << n) -1:
        if graphs[now][0] != 0:
            dp[now][visited] = graphs[now][0]
            return graphs[now][0]
        else:
            return sys.maxsize

    if dp[now][visited] != -1:
        return dp[now][visited]

    minDst = sys.maxsize
    for nxt in range(n):
        if graphs[now][nxt] == 0 or visited & ( 1 << nxt):
            continue
        minDst = min(minDst,dfs(nxt,visited | ( 1 << nxt )) + graphs[now][nxt])
    dp[now][visited] = minDst
    return dp[now][visited]

n = int(input())
graphs = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*(1 << n) for _ in range(n)]

print(dfs(0,1))
