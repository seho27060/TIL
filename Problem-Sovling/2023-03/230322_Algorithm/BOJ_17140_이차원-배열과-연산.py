#230321 17140 이차원 배열과 연산
# 행 개수 >= 열 개수 -> 행 연산
# 아니면 열 연산
import copy
import sys
from collections import defaultdict

# 숫자 할당하면서 자르기./
input = sys.stdin.readline

def rowCalculation(board):
    result = []
    maxLen = 0
    for row in range(len(board)):
        numDict = defaultdict(int)

        for idx in range(len(board[row])):
            if board[row][idx] != 0:
                numDict[board[row][idx]] += 1
        items = sorted(numDict.items(),key=lambda x:(x[1],x[0]))
        ouput = []
        for item in items:
            ouput.extend(item)
        result.append(ouput[:100])
        maxLen = max(maxLen,len(ouput))

    maxLen = min(100,maxLen)

    for row in range(len(result)):
        for col in range(maxLen-len(result[row])):
            result[row].append(0)

    return result

def colCalculation(board):
    result = []
    maxLen = 0
    for col in range(len(board[0])):
        numDict = defaultdict(int)

        for idx in range(len(board)):
            if board[idx][col] != 0:
                numDict[board[idx][col]] += 1
        items = sorted(numDict.items(), key=lambda x: (x[1], x[0]))
        ouput = []
        for item in items:
            ouput.extend(item)
        result.append(ouput[:100])
        maxLen = max(maxLen, len(ouput))
    maxLen = min(100, maxLen)

    for row in range(len(result)):
        for col in range(maxLen - len(result[row])):
            result[row].append(0)

    resutlConvert = [[] for _ in range(len(result[0]))]

    for row in range(len(result)):
        for col in range(len(result[0])):
            resutlConvert[col].append(result[row][col])

    return resutlConvert


r, c, k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(3)]

# (r,c) 자리의 board[r-1][c-1]의 값이 k가 되는데 걸리는 시간 출력

answer = 0

while answer <= 100:
    # for bb in board:
    #     print(bb)
    # print()
    if len(board) >= r and len(board[0]) >= c:
        if board[r-1][c-1] == k:
            break
        else:
            answer += 1
    else:
        answer += 1

    if len(board) >= len(board[0]): # 행 연산
        board = copy.deepcopy(rowCalculation(board))
    else: # 열 연산
        board = copy.deepcopy(colCalculation(board))

if answer > 100:
    answer = -1
print(answer)