# 230206 2887 행성 터널
# n개 행성이 있다. 서로 연결할려고 하는데, n-1개 간선으로 모두 연결할려고 한다.
# 최소 비용 구하라
# n*n짜리 비용 구하기. -> 대각선 나누고 위쪽만 구하면?..
# n*n-1*n-2...
# 심지어 축이 3개네?

import sys
from heapq import *

input = sys.stdin.readline

def calculateDist(a,b):
    return min(abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]))

n = int(input())

planets = [list(map(int,(input()+" "+str(idx)).split())) for idx in range(n)]
planetX = sorted(planets,key=lambda x:x[0])
planetY = sorted(planets,key=lambda x:x[1])
planetZ = sorted(planets,key=lambda x:x[2])

graphs = [[] for _ in range(n)]
# 와 축이 3개면. 각 축마다 가장 가까운 행성은 1개씩..
# 그럼 간선이 3*n이네..
for idx in range(n-1):
    cost = calculateDist(planetX[idx][:3], planetX[idx + 1][:3])
    start, end = planetX[idx][3],planetX[idx + 1][3]
    graphs[start].append((cost,end))
    graphs[end].append((cost,start))
    cost = calculateDist(planetY[idx][:3], planetY[idx + 1][:3])
    start, end = planetY[idx][3], planetY[idx + 1][3]
    graphs[start].append((cost, end))
    graphs[end].append((cost, start))
    cost = calculateDist(planetZ[idx][:3], planetZ[idx + 1][:3])
    start, end = planetZ[idx][3], planetZ[idx + 1][3]
    graphs[start].append((cost, end))
    graphs[end].append((cost, start))

queue = []
heappush(queue,(0,0))
answer = 0
visited = [0]*n
count = 0
while queue:
    cost, now = heappop(queue)
    if count == n:
        break
    if visited[now] == True:
        continue
    answer += cost
    # print(cost,now)
    visited[now] = 1
    count += 1
    for nxt in graphs[now]:
        heappush(queue,nxt)
# print(visited)
print(answer)