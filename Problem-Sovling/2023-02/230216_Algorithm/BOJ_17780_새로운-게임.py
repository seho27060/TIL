# 230216 17780 새로운 게임
# n*n 보드, k개의 말, 말위에 말 얹을 수 있음. 횐 빨 파 로 구성
# 1 ~ k번 말, 상하좌우 이동
# 턴 한번에 말들을 정해진 방향으로 이동시킴. 같은 칸의 가장 밑만 이동가능

# 시간복잡도보다는 구현이 복잡

import sys

input = sys.stdin.readline


def pieceMove(nowR, nowC,check):
    global pieces, moves, board, answer
    piece = pieces[nowR][nowC][0]
    move = moves[piece[1]]
    nxtR, nxtC = nowR + move[0], nowC + move[1]
    if 0 <= nxtR < n and 0 <= nxtC < n:
        if board[nxtR][nxtC] == 0:  # white
            pieces[nxtR][nxtC].extend(pieces[nowR][nowC])
            # if len(pieces[nxtR][nxtC]) >= 4:
            #     print(answer)
            #     exit()
            pieces[nowR][nowC] = []
            return 0
        elif board[nxtR][nxtC] == 1:  # red
            pieces[nxtR][nxtC].extend(reversed(pieces[nowR][nowC]))
            # if len(pieces[nxtR][nxtC]) >= 4:
            #     print(answer)
            #     exit()
            pieces[nowR][nowC] = []
            return 1
        elif board[nxtR][nxtC] == 2 and check == 0:  # blue
            direct = piece[1]
            if direct == 0:
                direct = 1
            elif direct == 1:
                direct = 0
            elif direct == 2:
                direct = 3
            elif direct == 3:
                direct = 2
            pieces[nowR][nowC][0] = [piece[0], direct]
            return 2
    else:
        # blue
        if check == 0:
            direct = piece[1]
            if direct == 0:
                direct = 1
            elif direct == 1:
                direct = 0
            elif direct == 2:
                direct = 3
            elif direct == 3:
                direct = 2
            pieces[nowR][nowC][0] = [piece[0], direct]
            return 2

# 블루 -> 블루일때 방향전환은 1번으로 끝나야됨.
n, k = map(int, input().split())
# 0 w/1 r/2 b
board = [list(map(int, input().split())) for _ in range(n)]
# 1234 = 우좌상하
pieces = [[[] for i in range(n)] for j in range(n)]
for idx in range(k):
    r, c, m = map(int, input().split())
    pieces[r - 1][c - 1].append([idx, m - 1])


answer = 0
moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
while answer <= 1000:
    answer += 1

    for idx in range(k):
        row, col = -1, -1

        for r in range(n):
            for c in range(n):
                if pieces[r][c]:
                    if pieces[r][c][0][0] == idx:
                        row, col = r, c
                        break
            if row != -1:
                break

        if row != -1 and col != -1:
            result = pieceMove(row, col,0)
            if result == 2:
                pieceMove(row, col,1)

    for row in range(n):
        for col in range(n):
            if len(pieces[row][col]) >= 4:
                print(answer)
                exit()
if answer >= 1000:
    print(-1)
