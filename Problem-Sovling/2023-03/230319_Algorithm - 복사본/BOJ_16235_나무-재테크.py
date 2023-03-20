# 230320 16235 나무 재테크
# n*n개 칸의 각각의 양분을 갖는 땅에
# m개의 나무를 심음, 각 칸마다 나무 개수 다름
# 봄에 나이만큼 양분 흡수, 나이 1 증가
# 여러나무있으면 어린나무부터 양분 흡수, 양분 나이만큼 못먹으면 즉사
# 여름에 봄에 죽은 나무가 양분으로 변함, 나이//2 = 변한 양분
# 가을에 나무 번식, 5의 배수면 번식, 인접 8칸에 나이가 1인 나무 생김
# 겨울에는 기계까 돌아댕김서 양분 뿌림, 입력대로
# k년 후, 살아있는 나무의 개수를 구하라....
# 칸마다 나무를..줘야하나?...

# n <= 10, m <= n**2... 작은거보니 구현

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int,input().split())

board = [] # 땅
nutrient = [] # 겨울마다 각 칸에 뿌리는 양분

for _ in range(n):
    board.append([5]*n)
    nutrient.append(list(map(int,input().split())))

trees = [[deque([]) for row in range(n)] for col in range(n)]

for _ in range(m):
    x, y, age = map(int,input().split())
    trees[x-1][y-1].append(age)
# 나이:좌표list의 dict로?...
for year in range(k):
    # spring
    deadTrees = [] # row, col, age
    for row in range(n):
        for col in range(n):
            nowNutrient = board[row][col]
            for idx in range(len(trees[row][col])):
                nowTree = trees[row][col].popleft()
                if nowNutrient >= nowTree:
                    nowNutrient -= nowTree
                    trees[row][col].append(nowTree+1)
                else:
                    deadTrees.append([row,col,nowTree])
            board[row][col] = nowNutrient
    # summer
    for x,y,age in deadTrees:
        board[x][y] += age//2
    # fall
    for row in range(n):
        for col in range(n):
            for age in trees[row][col]:
                if age % 5 == 0:
                    for addR in [-1,0,1]:
                        for addC in [-1,0,1]:
                            if not (addR == 0 and addC == 0) and (0 <= row + addR < n and 0<= col + addC <n):
                                trees[row+addR][col+addC].appendleft(1)

    # winter
    for row in range(n):
        for col in range(n):
            board[row][col] += nutrient[row][col]

answer = 0
for row in range(n):
    for col in range(n):
        answer += len(trees[row][col])

print(answer)