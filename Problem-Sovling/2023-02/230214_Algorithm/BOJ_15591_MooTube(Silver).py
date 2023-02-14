# 230214 15591 MonnTube(Silver)
# 그래프, 간선간 비용,
# n < 5,000

import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int,input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e, r = map(int,input().split())
    graphs[s].append([r,e])
    graphs[e].append([r,s])

result = [0]
for start in range(1,n+1):
    visited = [-1]*(n+1)
    visited[start] = sys.maxsize

    queue = deque([start])
    while queue:
        now = queue.popleft()

        for nxt in graphs[now]:
            [cost,cow] = nxt
            if visited[cow] == -1:
                visited[cow] = min(visited[now],cost)
                queue.append(cow)
    result.append(visited)

for _ in range(q):
    k, v = map(int,input().split())
    cnt = 0
    for end in range(1,n+1):
        if end != v and result[v][end] >= k:
            cnt += 1
    print(cnt)
