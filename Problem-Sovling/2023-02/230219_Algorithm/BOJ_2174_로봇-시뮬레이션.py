# 230219 2174 로봇 시뮬레이션

# a*b <= 10,000 board에 n<100개의 로봇이 있다.
# m <= 100개의 명령을 수행하는데 잘못된 경우를 출력하고
# 없으면 ok 출력

import sys

input = sys.stdin.readline

def findRowCol(idx):
    global board, a, b
    for r in range(b):
        for c in range(a):
            if board[r][c]:
                if board[r][c][0] == idx:
                    return [r,c,board[r][c][1]]

a, b = map(int,input().split())
n, m = map(int,input().split())

board = [[[] for i in range(a)] for j in range(b)]
moves = [[0,1],[-1,0],[0,-1],[1,0]]
ewsn = ["E","S","W","N"]

for idx in range(n):
    getStr = list(input().split())
    board[int(getStr[1])-1][int(getStr[0])-1]= [idx+1,getStr[2]]

for _ in range(m):

    getStr = list(input().split())
    # print(getStr)
    # for bb in board:
    #     print(bb)
    # print()
    [nowR,nowC,direction] = findRowCol(int(getStr[0]))


    if getStr[1] == "F":
        for cnt in range(int(getStr[2])):
            dirIdx = ewsn.index(direction)
            nxtR, nxtC = nowR + moves[dirIdx][0], nowC + moves[dirIdx][1]

            if 0 <= nxtR < b and 0 <= nxtC < a:
                if board[nxtR][nxtC]:
                    print("Robot {0} crashes into robot {1}".format(int(getStr[0]), board[nxtR][nxtC][0]))
                    exit()
                else:
                    board[nxtR][nxtC] = [int(getStr[0]), ewsn[dirIdx]]
                    board[nowR][nowC] = []
                    nowR, nowC = nxtR, nxtC
            else:
                print("Robot {0} crashes into the wall".format(getStr[0]))
                exit()
    elif getStr[1] == "L":
        dirIdx = ewsn.index(direction)
        dirIdx -= 1*(int(getStr[2])%4)
        if dirIdx < 0:
            dirIdx += 4
        board[nowR][nowC][1] = ewsn[dirIdx]
    elif getStr[1] == "R":
        dirIdx = ewsn.index(direction)
        dirIdx += 1*(int(getStr[2])%4)
        if dirIdx > 3:
            dirIdx -= 4
        board[nowR][nowC][1] = ewsn[dirIdx]
print("OK")
