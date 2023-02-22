# 230222 16234 인구 이동

import sys
from collections import deque

input = sys.stdin.readline

def bfs(row,col,idx):
    global board, n, l, r, unions, moves

    result = set()

    queue = deque([[row,col]])

    while queue:
        nowR, nowC = queue.popleft()
        result.add((nowR,nowC))
        unions[nowR][nowC] = idx

        for move in moves:
            nxtR, nxtC = nowR + move[0], nowC + move[1]

            if 0 <= nxtR < n and 0 <= nxtC < n:
                if l <= abs(board[nowR][nowC] - board[nxtR][nxtC]) <= r and (nxtR,nxtC) not in result and unions[nxtR][nxtC] == 0:
                    queue.append([nxtR,nxtC])
                    result.add((nxtR,nxtC))
    if len(result) > 1:
        return result
    else:
        return


n, l, r = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]

# 전체 좌표 탐색하면서,
# bfs로 인구차이가 l 이상 r 이하인 연합 찾고
# 연합의 인구수 계산 후 분배. 인구 재배치
# 다시 반복

day = 0

while 1:
    unions = [[0] * n for _ in range(n)]
    unionIdx = 1

    unionResults = []
    for row in range(n):
        for col in range(n):
            if unions[row][col] == 0:
                result = bfs(row,col,unionIdx)
                unionIdx += 1
                if result:
                    unionResults.append(result)

    if unionResults:
        for unionResult in unionResults:
            people = 0

            for loc in unionResult:
                people += board[loc[0]][loc[1]]
            people = int(people/len(unionResult))
            for loc in unionResult:
                board[loc[0]][loc[1]] = people
    else:
        break
    day += 1

print(day)
