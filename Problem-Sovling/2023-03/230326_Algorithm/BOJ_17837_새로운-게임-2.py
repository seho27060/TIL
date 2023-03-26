# 230326 17837 새로운 게임 2
# n*n 격자 위에 k개의 횐/빨/파 색의 말이 있다.
# 말 위에 다른 말을 얹을 수도 있고, 각 말의 방향을 갖음
# 1 턴은 1~k번 말을 이동. 말이 이동하면 얹어진 다른 말도 같이 이동
# 말이 4개 이상 쌓이면 game over
# 이동하려는 칸이
# 횐색 - 그냥 이동, 쌓인 말 그대로 다 같이 이동
# 빨간색 - 순서를 뒤바꿔서 얹는다.
# 파란색, 범위밖 - 이동방향 반대로 하고 이동, 또 파란색 or 범위밖이면 이동안하고 그대로있음
# game over 턴을 구하라
import copy
import sys
from collections import deque

input = sys.stdin.readline

def chessMove(nowPiece,blueCnt):
    global moves, chess, board, pieces, turn

    move = moves[nowPiece[2]]

    nowR, nowC = nowPiece[0], nowPiece[1]
    nxtR, nxtC = nowR + move[0], nowC + move[1]

    nowChess = []
    for chessIdx in range(len(chess[nowR][nowC])):
        if chess[nowR][nowC][chessIdx] == idx:
            nowChess.extend(chess[nowR][nowC][chessIdx:])
            chess[nowR][nowC] = copy.deepcopy(chess[nowR][nowC][:chessIdx])
            break

    if 0 <= nxtR < n and 0 <= nxtC < n:
        if board[nxtR][nxtC] == 0:
            chess[nxtR][nxtC].extend(nowChess)
            for nowChessIdx in nowChess:
                pieces[nowChessIdx][0] = nxtR
                pieces[nowChessIdx][1] = nxtC
            if len(chess[nxtR][nxtC]) >= 4:
                print(turn)
                exit()
        elif board[nxtR][nxtC] == 1:
            nowChess.reverse()
            chess[nxtR][nxtC].extend(nowChess)
            for nowChessIdx in nowChess:
                pieces[nowChessIdx][0] = nxtR
                pieces[nowChessIdx][1] = nxtC
            if len(chess[nxtR][nxtC]) >= 4:
                print(turn)
                exit()
        elif board[nxtR][nxtC] == 2:
            if blueCnt == 0:
                if nowPiece[2] == 1:
                    nxtD = 2
                elif nowPiece[2] == 2:
                    nxtD = 1
                elif nowPiece[2] == 3:
                    nxtD = 4
                elif nowPiece[2] == 4:
                    nxtD = 3
                pieces[idx][2] = nxtD
                nxtPiece = copy.deepcopy(pieces[idx])
                chess[nowR][nowC].extend(nowChess)
                chessMove(nxtPiece,1)
            elif blueCnt == 1:
                chess[nowR][nowC].extend(nowChess)

    else:
        if blueCnt == 0:
            if nowPiece[2] == 1:
                nxtD = 2
            elif nowPiece[2] == 2:
                nxtD = 1
            elif nowPiece[2] == 3:
                nxtD = 4
            elif nowPiece[2] == 4:
                nxtD = 3
            pieces[idx][2] = nxtD
            nxtPiece = copy.deepcopy(pieces[idx])
            chess[nowR][nowC].extend(nowChess)
            chessMove(nxtPiece, 1)
        elif blueCnt == 1:
            chess[nowR][nowC].extend(nowChess)

n, k = map(int,input().split())

# 0 W/ 1 R/ 2 B
board = [list(map(int,input().split())) for _ in range(n)]
chess = [[[] for r in range(n)] for c in range(n)]

moves = [[],[0,1],[0,-1],[-1,0],[1,0]] # 1 2/ 3 4
pieces = []

for piece in range(k):
    r, c, d = map(int,input().split())
    pieces.append([r-1,c-1,d])
    chess[r-1][c-1].append(piece)

turn = 1

while turn <= 1000:
    # print(turn,pieces)
    # for idx in range(n):
    #     print(chess[idx])
    for idx in range(len(pieces)):
        piece = copy.deepcopy(pieces[idx])
        chessMove(piece,0)
    turn += 1

if turn > 1000:
    turn = -1

print(turn)
