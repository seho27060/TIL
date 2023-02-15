# 230215 14666 소가 길을 건너간 이유 6

import sys
from collections import deque
from itertools import combinations

# (0,0)에서 bfs 시행. visited 체크
# cows중에 visited에 체크 안된 애들은 절대 못감 -> 빼고
# 경우의 수(조합) 카운트

input = sys.stdin.readline

def bfs(start):
    global n, roads, visited, moves,answer

    queue = deque([start])
    visited[start[0]][start[1]] = 1

    while queue:
        now = queue.popleft()

        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]

            if 0 <= nxtR < n and 0 <= nxtC < n:
                if visited[nxtR][nxtC] == 0 and [nxtR,nxtC] not in roads[now[0]][now[1]]:
                    queue.append([nxtR,nxtC])
                    visited[nxtR][nxtC] = 1
                    answer.add((tuple(start),(nxtR,nxtC)))


n, k, r = map(int,input().split())
roads = [[[] for i in range(n)] for j in range(n)]

for _ in range(r):
    a,b, x,y = map(int,input().split())
    roads[a-1][b-1].append([x-1,y-1])
    roads[x-1][y-1].append([a-1,b-1])

cows = []

for _ in range(k):
    x, y = list(map(int,input().split()))
    cows.append((x-1,y-1))

startToEnd = set(combinations(cows,2))

answer = set()
moves = [[0,1],[0,-1],[1,0],[-1,0]]
for cow in cows:
    visited = [[0]*n for _ in range(n)]
    if visited[cow[0]][cow[1]] == 0:
        bfs(cow)

print(len(startToEnd.difference(answer)))