# 230327 17822 원판 돌리기
# 원판에 수가 있는데 상하좌우로 인접함
# i번째 원판의 j번째 수. 원판마다 m개가 있음

import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int,input().split())

board = [0]
arounds = [[-1,0],[1,0],[0,1]]
for _ in range(n):
    board.append(deque(list(map(int, input().split()))))
    # 1 -> m, m -> 1해야하니까 deque으로 관리

# 번호가 x의 배수인 원판을 d방향(0 = 시계, 1 = 반시계)로 k칸 회전
for _ in range(t):
    x, d, k = map(int,input().split())

    # 명령대로 원판 돌리기
    for row in range(1,n+1):
        share, remain = divmod(row,x)
        if share >= 1 and remain == 0:
            # 돌리면서 확인? 다 돌리고 확인?
            for move in range(k):
                if d == 1:
                    num = board[row].popleft()
                    board[row].append(num)
                elif d == 0:
                    num = board[row].pop()
                    board[row].appendleft(num)

    # 돌리고 돌려진 행 인접 요소 삭제 or 업데이트
    deleteSet = set()
    for row in range(1,n+1):
        for col in range(m):
            check = False
            if board[row][col] != 0:
                for around in arounds:
                    nxtR, nxtC = row + around[0], (col + around[1])%m
                    if 1 <= nxtR <= n:
                        if board[row][col] == board[nxtR][nxtC]:
                            deleteSet.add((nxtR,nxtC))
                            check = True
            if check:
                deleteSet.add((row,col))
    if deleteSet:
        for r, c in deleteSet:
            board[r][c] = 0
    else:
        average = 0
        cnt = 0
        for r in range(1,n+1):
            for c in range(m):
                if board[r][c] != 0:
                    average += board[r][c]
                    cnt += 1
        if cnt >= 1:
            average /= cnt

            for r in range(1,n+1):
                for c in range(m):
                    if board[r][c] != 0:
                        if board[r][c] > average:
                            board[r][c] -= 1
                        elif board[r][c] < average:
                            board[r][c] += 1
answer = 0
for r in range(1,n+1):
    answer += sum(board[r])
print(answer)
