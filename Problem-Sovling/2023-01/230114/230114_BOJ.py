import sys

input = sys.stdin.readline

def bfs(r,c):
    global result, n, m, board

    moves = [[0,1],[1,0],[-1,0],[0,-1]]

    queue = [[r,c]]
    visited[r][c] = 1

    while queue:
        nowR, nowC = queue.pop()
        visited[nowR][nowC] = 1

        for move in moves:
            nxtR, nxtC = nowR + move[0], nowC + move[1]
            if nxtR < 0:
                nxtR = n - 1
            elif nxtR >= n:
                nxtR = 0
            if nxtC < 0:
                nxtC = m - 1
            elif nxtC >= m:
                nxtC = 0
            if board[nxtR][nxtC] == 0 and visited[nxtR][nxtC] == 0 :
                queue.append([nxtR,nxtC])

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
result = 0

for row in range(n):
    for col in range(m):
        if board[row][col] == 0 and visited[row][col] == 0:
            result += 1
            bfs(row,col)

print(result)


