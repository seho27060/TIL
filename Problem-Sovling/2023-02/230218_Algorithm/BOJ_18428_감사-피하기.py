# 230218 18428 감시 피하기

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

board = [list(input().split()) for _ in range(n)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]

teachers = []
spaces= set()
for row in range(n):
    for col in range(n):
        if board[row][col] == "T":
            teachers.append([row,col])
            for idx in range(1,n):
                for move in moves:
                    nxtR, nxtC = row + move[0]*idx, col + move[1]*idx
                    if 0 <= nxtR < n and 0 <= nxtC < n:
                        if board[nxtR][nxtC] == "X":
                            spaces.add((nxtR,nxtC))

answer = "NO"
combis = list(combinations(spaces,3))
for combi in combis:

    for com in combi:
        board[com[0]][com[1]] = "O"

    # print(combi)
    # for b in board:
    #     print(b)
    result = True
    for teacher in teachers:
        row, col = teacher

        for move in moves:
            check = False
            for idx in range(1, n):
                nxtR, nxtC = row + move[0] * idx, col + move[1] * idx
                if 0 <= nxtR < n and 0 <= nxtC < n:
                    if board[nxtR][nxtC] == "S":
                        result = False
                        break
                    elif board[nxtR][nxtC] == "O":
                        check = True
                        break

                if result is False or check:
                    break
            if result is False:
                break

    if result:
        print("YES")
        exit()
    for com in combi:
        board[com[0]][com[1]] = "X"

print("NO")

