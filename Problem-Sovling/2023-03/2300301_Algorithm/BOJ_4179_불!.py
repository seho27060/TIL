#230301 4179 불!
# n*n < 1,000,000 인 보드에 사람과 불이 있다.
# 사람이 불을 피해 탈출 가능한지 출력하라
import copy
# 사람과 불의 이동은 bfs로..
# 백트래킹?..
# 불의 이동방향은 고정이니깐,, 가능한 보드의 칸 내에서 탐색 이동
# 범위 끝으로가면 -> 탈출
# 한턴 -> 지훈과 불 모두 이동 -> 지훈, 불 순서로 이동
# 지훈 리스트와 불 리스트가 있어야..하나?
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global r, c, board, jihun, fires, moves,answer

    while jihun:
        nxtJihun = set()
        nxtFires = set()

        for now in jihun:
            if board[now[0]][now[1]] != "#":
                for move in moves:
                    nxtR, nxtC = now[0] + move[0], now[1] + move[1]
                    if 0 <= nxtR < r and 0 <= nxtC < c:
                        if board[nxtR][nxtC] != "#" and (board[nxtR][nxtC] == 0 or board[nxtR][nxtC] > board[now[0]][now[1]] + 1):
                            board[nxtR][nxtC] = board[now[0]][now[1]] + 1
                            nxtJihun.add((nxtR,nxtC))
                    else:
                        answer = min(answer,board[now[0]][now[1]])

        for now in fires:
            for move in moves:
                nxtR, nxtC = now[0] + move[0], now[1] + move[1]
                if 0 <= nxtR < r and 0 <= nxtC < c:
                    if board[nxtR][nxtC] != "#":
                        board[nxtR][nxtC] = "#"
                        nxtFires.add((nxtR,nxtC))

        jihun = copy.deepcopy(nxtJihun)
        fires = copy.deepcopy(nxtFires)

r, c = map(int,input().split())

board = [list(input().rstrip()) for _ in range(r)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]

jihun = set()
fires = set()
answer = sys.maxsize

for row in range(r):
    for col in range(c):
        if board[row][col] == "J":
            jihun.add((row,col))
            board[row][col] = 1
        elif board[row][col] == "F":
            fires.add((row,col))
            board[row][col] = "#"
        elif board[row][col] == ".":
            board[row][col] = 0

bfs()

if answer >= sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(answer)