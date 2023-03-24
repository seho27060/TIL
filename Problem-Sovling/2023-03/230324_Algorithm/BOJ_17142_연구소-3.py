# 230324 17142 연구소 3
# bfs 적으로... 한 사이클 마다 이동(감영)해야할듯
# 바이러스 개수 1 <= m <= 10, m<=바이러스 놓을수 있는 자리개수 <=10 일때
# 경우의 수가 많이 생기네요.. 최대 10!
import copy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def bfs(nowVirues):
    global n, lab, moves, answer, resultTime, checkCnt, resultCnt

    if resultCnt >= checkCnt:
        resultCheck = True
        for row in range(n):
            for col in range(n):
                if lab[row][col] == 0:
                    resultCheck = False
                    break
            if resultCheck == False:
                break
        if resultCheck:
            answer = min(answer,resultTime)
        return
    if nowVirues:
        nxtVirues = []
        for virus in nowVirues:
            for move in moves:
                nxtR, nxtC = virus[0] + move[0], virus[1] + move[1]
                if 0 <= nxtR < n and 0 <= nxtC < n:
                    if lab[nxtR][nxtC] in [0,2]:
                        if lab[nxtR][nxtC] == 0:
                            resultCnt += 1
                        lab[nxtR][nxtC] = 3
                        nxtVirues.append([nxtR,nxtC])
        resultTime += 1
        bfs(nxtVirues)
    else:
        return

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]
viruses = []
checkCnt = n*n
for row in range(n):
    for col in range(n):
        if board[row][col] == 2:
            viruses.append([row,col])
            checkCnt -= 1
        if board[row][col] == 1:
            checkCnt -= 1

answer = sys.maxsize

candidates = list(combinations(viruses,m))

for candidate in candidates:
    lab = copy.deepcopy(board)
    resultTime = 0
    resultCnt = 0
    for [row,col] in candidate:
        lab[row][col] = 3
    bfs(candidate)

if answer >= sys.maxsize:
    answer = -1

print(answer)