# 230127 17143 낚시왕
# 구현 문제
# 낚시왕은 한번만 쓱 훑고 지나가면 끝이다.

# 낚시왕 이동 -> 상어 이동
# 상어가 한자리 모이면 큰놈이 잡아먹음

import sys

input = sys.stdin.readline

r, c, m = map(int,input().split())

# r c s d z
sharks = [list(map(int,input().split())) for _ in range(m)]
# 상하우좌 1234
moves = [[],[-1,0],[1,0],[0,1],[0,-1]]
answer = 0

for fishingMaster in range(1,c+1):
    sharkIdxInNet = []

    for sharkIdx in range(len(sharks)):
        shark = sharks[sharkIdx].copy()
        if shark[1] == fishingMaster:
            sharkIdxInNet.append(shark)
    # print("!",sharkIdxInNet,">",sharks)
    if sharkIdxInNet:
        sharkIdxInNet.sort(key=lambda x:x[0])
        answer += sharkIdxInNet[0][4]
        sharks.remove(sharkIdxInNet[0])

    board = [[[] for i in range(c+1)] for j in range(r+1)]
    for shark in sharks:
        nowR, nowC, s, d, z = shark
        move = moves[d]

        cnt = 0
        while cnt < s:
            nxtR, nxtC = nowR + move[0], nowC + move[1]

            if 1 <= nxtR <= r and 1 <= nxtC <= c:
                cnt += 1
                nowR, nowC = nxtR, nxtC
            else:
                if d == 1:
                    d = 2
                    move = moves[2]
                elif d == 2:
                    d = 1
                    move = moves[1]
                elif d == 3:
                    d = 4
                    move = moves[4]
                elif d == 4:
                    d = 3
                    move = moves[3]
        #     print("cnt",cnt,nxtR,nxtC,s,d,z)
        # print(nowR,nowC,board[nowR][nowC],[s,d,z])
        if board[nowR][nowC]:
            board[nowR][nowC] = [max(board[nowR][nowC][0],[s,d,z], key=lambda x:x[2])]
        else:
            board[nowR][nowC].append([s,d,z])

    sharks = []
    for row in range(r+1):
        for col in range(c+1):
            if board[row][col]:
                [s, d, z] = board[row][col][0]
                sharks.append([row,col,s,d,z])

print(answer)





