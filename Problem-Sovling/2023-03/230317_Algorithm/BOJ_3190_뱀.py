# 230317 3190 뱀
# 아이템먹으면 길이가 길어지는 뱀게임 구현
# (0,0)에서 시작해서 오른쪽 방향
# 사과먹으면 길이 길어짐

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for apple in range(k):
    row, col = map(int,input().split())
    board[row-1][col-1] = 1

l = int(input())
dirChanges = deque([])
for _ in range(l):
    time, direct = input().split(" ")
    dirChanges.append([int(time),direct.rstrip()])

moves = [[0,1],[1,0],[0,-1],[-1,0]] # 우 하 좌 상

answer = 0
snake = deque([[0,0]])
direct = 0
dirChange = dirChanges.popleft()
# 머리(인덱스 0) 가져와서(pop아님) direct대로 탐색
# 사과있으면, 그대로 머리로 추가
# 없으면, 추가하고 꼬리(인덱스 마지막) pop
while 1:
    answer += 1

    head = snake[0].copy()

    nxtR, nxtC = head[0] + moves[direct][0], head[1] + moves[direct][1]

    if 0 <= nxtR < n and 0 <= nxtC < n:

        if board[nxtR][nxtC] == 1:#사과있음
            board[nxtR][nxtC] = 0
        elif [nxtR,nxtC] in snake:
            break
        else:#사과없음
            snake.pop()
        snake.insert(0, [nxtR, nxtC])
    else:
        break

    # 방향 전환
    if dirChange:
        if answer == dirChange[0]:
            if dirChange[1] == "L":
                direct -= 1
            elif dirChange[1] == "D":
                direct += 1

            direct += 4
            direct = direct%4

            if dirChanges:
                dirChange = dirChanges.popleft()
            else:
                dirChange = []

print(answer)

