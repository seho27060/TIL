# 230203 4386 별자리 만들기
# n < 100, n개 점 MST?
# i*j 행렬 구하고 서로 거리 구하고..
# 최소비용으로 잇는 거 구하기..?

import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]

board = [[0]*(n) for _ in range(n)]

for start in range(n):
    for end in range(n):
        board[start][end] = (abs(points[start][0]-points[end][0])**2+abs(points[start][1]-points[end][1])**2)**0.5

queue = []
heappush(queue,(0.0,0))
visited = set()
answer = 0

while queue:
    dst,now = heappop(queue)
    if now in visited:
        continue
    visited.add(now)
    answer += dst

    for nxt in range(n):
        if nxt not in visited and board[now][nxt] != 0:
            heappush(queue,(board[now][nxt],nxt))

print(round(answer,2))