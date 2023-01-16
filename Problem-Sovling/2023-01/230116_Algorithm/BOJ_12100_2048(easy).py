# 230112 BOJ 12100 2048(Easy)

# 2048게임의 작동과정을 구현해보자
# n <= 20. n*n 보드 제공
# 블록의 값은 2 <= x <= 1024

# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출려하라
# -> 구현, 백트래킹

import sys

input = sys.stdin.readline

def backtrack(count):
    global n, board, moves, result

    count += 1

    blocks = []
    for row in range(n):
        for col in range(n):
            if board[row][col] != 0:
                blocks.append([row,col,board[row][col]])
    if count <= 5:
        for direction in range(4):
            if direction == 0:
                blocks.sort(key=lambda x: x[0])
            elif direction == 1:
                blocks.sort(key=lambda x: x[1])
            elif direction == 2:
                blocks.sort(key=lambda x: -x[0])
            elif direction == 3:
                blocks.sort(key=lambda x: -x[1])

            nxtBlocks = []
            move = moves[direction]

            for block in blocks:
                row, col , score = block
                if score == board[row][col]:
                    board[row][col] = 0
                    nxtR, nxtC = row, col
                    check = False

                    while 1:
                        nxtR, nxtC = nxtR + move[0], nxtC + move[1]
                        if 0 <= nxtR < n and 0 <= nxtC < n and [nxtR,nxtC] not in nxtBlocks:
                            if board[nxtR][nxtC] == 0:
                                pass
                            elif board[nxtR][nxtC] == score:
                                score *= 2
                                check = True
                                break
                            else:
                                nxtR, nxtC = nxtR - move[0], nxtC - move[1]
                                break
                        else:
                            nxtR, nxtC = nxtR - move[0], nxtC - move[1]
                            break

                    board[nxtR][nxtC] = score
                    if check:
                        nxtBlocks.append([nxtR,nxtC])

            backtrack(count)

            for row in range(n):
                for col in range(n):
                    result = max(result,board[row][col])
                    board[row][col] = 0

            for block in blocks:
                row, col, score = block
                board[row][col] = score


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
result = 0

moves = [[-1,0],[0,-1],[1,0],[0,1]]

# 상좌하우 = 0,1,2,3

backtrack(0)
print(result)

