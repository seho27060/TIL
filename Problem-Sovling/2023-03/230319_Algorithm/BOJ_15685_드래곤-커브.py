# 230319 15685 드래곤 커브
# i세대 드래곤 커브는 i-1세대 드래곤커브를 시계 방향으로 90도 회전하여
# i세대 드래곤 커브의 끝점에 이어 붙인것이다.
# 100*100의 격자에 드래곤 커브가 n개 있다.
# 4개 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하라.
# * x는 -, y는 ㅣ
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
board = [[0]*101 for _ in range(101)]

moves = [[0,1],[-1,0],[0,-1],[1,0]] # 우 상 좌 하

dragonCurves = []
for _ in range(n):
    x, y, d, g = map(int,input().split())

    curves = []
    dragons = []
    # print(x,y,d,g)
    dragons.append((y, x))
    y, x = y + moves[d][0], x + moves[d][1]
    dragons.append((y, x))
    curves.append(d)
    for generation in range(g):
        newCurves = []
        for idx in range(len(curves)-1,-1,-1):
            newCurves.append((curves[idx]+1)%4)

        for newCurve in newCurves:
            y, x = y + moves[newCurve][0], x + moves[newCurve][1]
            dragons.append((y, x))
        curves.extend(newCurves)
    # print(curves)
    # print(dragons)
    for dragon in dragons:
        board[dragon[0]][dragon[1]] = 1
    # for bb in board[:10]:
    #     print(bb[:10])
answer = 0

for row in range(100):
    for col in range(100):
        if board[row][col] and board[row][col+1] and board[row+1][col] and board[row+1][col+1]:
            answer += 1
# print()
# for bb in board[:10]:
#     print(bb[:10])
print(answer)