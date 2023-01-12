# 230112 BOJ 13460 구슬탈출 2
# n*m =< 100
# 빨간 구슬, 파란 구슬있는데. 빨간 구슬빼내야함
# 파란구슬 빼내면 안됨
# 이리저리 굴려굴려
# 동시에 빠져도 실패
# 동시에 같은칸 있을 수 없어
# 구슬이 더이상움직이지않으면 기울일 수 없어
# 최소 몇번으로 구슬을 빼낼수 있을까?

# 백트래킹으로 상하좌우로 굴리고, 매번 굴릴때마다 공 2개의 위치 갱신
# 근데 좌로 굴리면 좌부터 쏴악 훑으면서 일직선으로 이동시켜야됨
# 작업 만들고
# 백트래킹으로 상좌하우 탐색
# 이동이 10번 초과하면 끝

import sys

input = sys.stdin.readline


def rolling(marbles, count):
    global moves, board, answer, n, m
    if count >= 11:
        return
    # for b in board:
    #     print(b)
    result = answer
    for moveIdx in range(4):
        # arrow = ["up","left","down","right"]
        # print("arrow is",arrow[moveIdx])
        if moveIdx == 0:  # 상
            marbles.sort(key=lambda x: x[0])
        elif moveIdx == 1:  # 좌
            marbles.sort(key=lambda x: x[1])
        elif moveIdx == 2:  # 하
            marbles.sort(key=lambda x: -x[0])
        elif moveIdx == 3:  # 우
            marbles.sort(key=lambda x: -x[1])

        move = moves[moveIdx]

        nxtMarbles = []
        moveCheck = True  # 다음이동 여부
        redCheck = False
        blueCheck = False
        for marble in marbles:
            nowR, nowC, color = marble[0], marble[1], board[marble[0]][marble[1]]
            for i in range(10):
                nxtR, nxtC = nowR + move[0], nowC + move[1]
                if 0 <= nxtR < n and 0 <= nxtC < m:
                    if board[nxtR][nxtC] == ".":
                        nowR, nowC = nxtR, nxtC
                    elif board[nxtR][nxtC] == "O":
                        moveCheck = False
                        # print("Puss!",i,nowR,nowC,nxtR,nxtC,color)
                        if color == "R":
                            result = count + 1
                            board[nowR][nowC] = "."
                            redCheck = True
                        elif color == "B":
                            blueCheck = True
                        break
                    else:
                        break
                else:
                    break
            board[marble[0]][marble[1]] = "."
            # print("!!",nowR,nowC,board[nowR][nowC],color)
            if (color == "R" and not redCheck) or (color =="B" and not blueCheck):
                board[nowR][nowC] = color
            nxtMarbles.append([nowR, nowC,color])

        # print(moveIdx, marbles, answer,result, nxtMarbles, moveCheck)
        # if redCheck:
        #     for b in board:
        #         print(b)
        if redCheck and not blueCheck:
            answer = min(answer,result)

        if moveCheck:
            if marbles[0] not in nxtMarbles or marbles[1] not in nxtMarbles:
                rolling(nxtMarbles, count + 1)

        for idx in range(2):
            board[nxtMarbles[idx][0]][nxtMarbles[idx][1]] = "."

        for idx in range(2):
            board[marbles[idx][0]][marbles[idx][1]] = marbles[idx][2]


n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 상좌하우
answer = sys.maxsize

red = []
blue = []

for row in range(n):
    for col in range(m):
        if board[row][col] == "R":
            red = [row, col, "R"]
        if board[row][col] == "B":
            blue = [row, col, "B"]
# print("red {0} and blue {1}".format(red, blue))
rolling([red, blue], 0)

if answer > 10:
    answer = -1
print(answer)
