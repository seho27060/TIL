# 230128 7579 앱
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
appMemories = [0] + list(map(int,input().split()))
appCosts = [0] + list(map(int,input().split()))

memories = [[0]*(sum(appCosts)+1) for _ in range(n+1)]

answer = sum(appCosts)

for idx in range(1,n+1):
    memory = appMemories[idx]
    cost = appCosts[idx]

    for money in range(1, sum(appCosts)+1):

        if money < cost:
            memories[idx][money] = memories[idx-1][money]
        else:
            memories[idx][money] = max(memory + memories[idx-1][money-cost], memories[idx-1][money])

        if memories[idx][money] >= m:
            answer = min(answer,money)

print(answer)
