# 230316 15683 감시
# 0 빈칸, 1~5 시시티비, 6 벽
# 1 한방향, 2 마주보는 방향, 3 90도, 4 1쪽빼고, 5 전체
# 시시티비는 벽통과는 못함, 근데 서로 통과는 됨
# 시시티비가 커버못하는 사각지대 최소 크기 출력
import sys

def backtrack(idx): # cctvs idx
    global n, m, direction, moves, board, cctvMovesList, cctvs, answer
    if idx >= len(cctvs):
        compare = 0
        for row in range(n):
            for col in range(m):
                if result[row][col] == 0 and board[row][col] == 0:
                    compare += 1

        if answer > compare:
            answer = compare
    else:
        r, c = cctvs[idx]

        cctvMoves = cctvMovesList[board[r][c]]

        for cctvMove in cctvMoves:
            moveMemo = []

            for moveIdx in cctvMove:
                move = moves[moveIdx]
                nxtR, nxtC = r, c
                while 0 <= nxtR < n and 0 <= nxtC < m:
                    nxtR, nxtC = nxtR + move[0], nxtC + move[1]

                    if 0 <= nxtR < n and 0 <= nxtC < m:
                        if board[nxtR][nxtC] != 6:
                            if board[nxtR][nxtC] == 0 and result[nxtR][nxtC] == 0:
                                result[nxtR][nxtC] = 1
                                moveMemo.append([nxtR,nxtC])
                        else:
                            break
                    else:
                        break
            backtrack(idx+1)
            for memo in moveMemo:
                result[memo[0]][memo[1]] = 0
n, m = map(int,input().split())
# 상, 우, 하, 좌
direction = [0,1,2,3]
moves= [[-1,0],[0,1],[1,0],[0,-1]]
cctvMovesList = [[],[[0],[1],[2],[3]],
             [[0,2],[1,3]],
             [[0,1],[1,2],[2,3],[3,0]],
             [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
             [[0,1,2,3]]]
board = [list(map(int,input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]

answer = sys.maxsize
cctvs = []

for row in range(n):
    for col in range(m):
        if 1 <= board[row][col] <= 5:
            cctvs.append([row,col])

backtrack(0)

print(answer)