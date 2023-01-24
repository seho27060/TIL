# 230124 1766 문제집
# 흠.. 유니온파인드 그래프?..

import sys
from heapq import *

input = sys.stdin.readline

def polygySort():
    global n, m, relation, problems
    result = []
    queue = []

    for s in range(1,n+1):
        if relation[s] == 0:
            heappush(queue,s)

    while queue:
        now = heappop(queue)
        result.append(now)

        for nxt in problems[now]:
            relation[nxt] -= 1
            if relation[nxt] == 0:
                heappush(queue,nxt)

    print(*result)
n, m = map(int,input().split())
relation = [0 for i in range(n+1)]
problems = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    problems[a].append(b)
    relation[b] += 1
# print(problems)
# print(relation)
polygySort()
