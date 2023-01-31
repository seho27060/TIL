# 230131 2239 스도쿠
# n = 9
# 0인 칸을 채우고 여러개의 답을 사전식으로 정렬하여 출력하라..

import sys
import copy
input = sys.stdin.readline

def sudoku(idx):
    global board, points, results

    if idx == len(points):
        results.append(copy.deepcopy(board))
        for res in results[0]:
            for re in res:
                print(re, end="")
            print()
        exit()

    [nowR, nowC] = points[idx]
    candidateNums = [0]*(10)
    for i in range(9):
        candidateNums[board[i][nowC]] += 1
        candidateNums[board[nowR][i]] += 1
    for nxtR in range((nowR)//3*3,(nowR)//3*3+3):
        for nxtC in range((nowC)//3*3,(nowC)//3*3+3):
            candidateNums[board[nxtR][nxtC]] += 1

    nums = []
    for num in range(1,10):
        if candidateNums[num] == 0:
            nums.append(num)

    if nums:
        for candidate in nums:
            board[nowR][nowC] = candidate
            sudoku(idx+1)
        board[nowR][nowC] = 0
    else:
        return

board = [list(map(int,list(input().rstrip()))) for _ in range(9)]
points = []

for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            points.append([row,col])

results = []
sudoku(0)

results.sort()

for res in results[0]:
    for re in res:
        print(re,end="")
    print()
