#230318 15684 사다리 조작
# 세로 선 개수 n <= 10, 놓을 수 있는 선 위치 h <= 30, 가로 선 개수 m <= (n-1)*h 일때
# i번 세로선의 사다리 결과가 i번이 나오도록 조작하려면..
# 추가해야하는 가로선의 최소 개수 출력
# 가로선들은 연속되거나 접하여 배치될 수 없음.

# 선하나 배치 할때마다 전체 bfs
# ladder : 가로선있으면 그쪽으로 이동, 아니면 아래로 이동할때 출발점과 도착점이 동일한가?
# 선 배치가 3되면 return
# 배치는 무조건 2개 이하

# 백트래킹으로..하다가.. 3이상이면 return?

def ladderGame():
    global board, n, h

    for start in range(n):
        col = start

        for row in range(h):
            if col - 1 >= 0 and board[row][col-1]:
                col -= 1
            elif col < n-1 and board[row][col]:
                col += 1
            else:
                pass
        if start != col:
            return False

    return True

from itertools import combinations

n, m, h = map(int,input().split())

board = [[0]*(n-1) for _ in range(h)]

for _ in range(m):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1

horizon = []

for row in range(h):
    for col in range(n-1):
        if board[row][col] == 0:
            horizon.append([row,col])

# for bb in board:
#     print(bb)

for lineCnt in range(4):
    candidates = list(combinations(horizon,lineCnt))
    for candidate in candidates:
        for [row,col] in candidate:
            board[row][col] = 1

        if ladderGame():
            print(lineCnt)
            exit()

        for [row,col] in candidate:
            board[row][col] = 0

print(-1)