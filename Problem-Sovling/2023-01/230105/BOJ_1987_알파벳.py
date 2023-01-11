# 230105 BOJ 1987 알파벳

# r,c = 20, 20
# 0,0에서 출발할때 연속되지 않는 알파벳을 지나며 최대로 이동할 수 있는 칸

import sys
from collections import deque

input = sys.stdin.readline


def checkAlphabet(record:list, nxt:str):
    result = True
    if nxt in record:
        result = False
    return result

def findWay():
    r, c = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(r)]

    result = [[[0,[]] for i in range(c)] for j in range(r)]
    result[0][0] = [1,[board[0][0]]] # 현재 record 길이, record 리스트
    answer = 1

    moves = [[1,0],[-1,0],[0,1],[0,-1]]

    queue = deque([[0,0]])

    while queue:
        now = queue.popleft()
        nowLen = result[now[0]][now[1]][0]
        if answer < nowLen:
            answer = nowLen
        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
            if 0 <= nxtR < r and 0 <= nxtC < c:
                alphabet = board[nxtR][nxtC]
                maxLen = result[nxtR][nxtC][0]
                check = False
                if nowLen + 1 == maxLen:
                    for record in result[now[0]][now[1]][1]:
                        if checkAlphabet(record,alphabet):
                            nxtRecord = record
                            nxtRecord += alphabet
                            if nxtRecord not in result[nxtR][nxtC][1]:
                                result[nxtR][nxtC][1].append(nxtRecord)
                                check = True
                elif nowLen + 1 > maxLen or maxLen == 0:
                    nxtRecords = []
                    for record in result[now[0]][now[1]][1]:
                        if checkAlphabet(record,alphabet):
                            nxtRecord = record
                            nxtRecord += alphabet
                            if nxtRecord not in nxtRecords:
                                nxtRecords.append(nxtRecord)
                                check = True
                    if check:
                        result[nxtR][nxtC] = [nowLen + 1, nxtRecords]
                if check and [nxtR,nxtC] not in queue:
                    queue.append([nxtR,nxtC])

    return answer
    # 지나온거 체크 -> 알파벳 체크

print(findWay())