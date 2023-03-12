# 230312 9527 1의 개수 세기
# n <50 짜리 정사각형 격자에
# 각 물이 채워져있고, 비바라기 주문이 실행됨
# 방향에 따라 이동하고 난 후 물이 채워지고 물복사버그가 진행
# 물복사버그 : 구름의 대각선 4개에 물이 있으면 그 격자 칸 개수만큼 구름자리의 물 증가
# m개 명령이 다 실행되고 나서 전체 물의 합을 출력
# 구름의 이동중 범위 넘어가면 끝에서 처음과 연결 순환구조
import copy
import sys

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

moves = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
# waterCheck = moves[1,3,5,7]
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
for _ in range(m):
    idx, dst = map(int,input().split())

    move = moves[idx-1]

    for cloudIdx in range(len(clouds)):
        clouds[cloudIdx][0] = (clouds[cloudIdx][0]+move[0]*dst)%n
        clouds[cloudIdx][1] = (clouds[cloudIdx][1]+move[1]*dst)%n
    for cloud in clouds:
        board[cloud[0]][cloud[1]] += 1

    cloudBoard= [[0]*n for nn in range(n)]

    # waterCheck
    for cloud in clouds:
        cnt = 0
        cloudBoard[cloud[0]][cloud[1]] = 1
        for waterCheck in [1,3,5,7]:
            nxtR, nxtC = cloud[0] + moves[waterCheck][0],cloud[1] + moves[waterCheck][1]
            if 0 <= nxtR < n and 0 <= nxtC < n:
                if board[nxtR][nxtC] > 0:
                    cnt += 1
        board[cloud[0]][cloud[1]] += cnt

    newClouds = []
    for row in range(n):
        for col in range(n):
            if board[row][col] >= 2 and cloudBoard[row][col] == 0:
                newClouds.append([row,col])
                board[row][col] -= 2
    clouds = copy.deepcopy(newClouds)

    # print(_+1)
    # for bb in board:
    #     print(bb)
    # print(clouds)
answer = 0
for row in range(n):
    answer += sum(board[row])
print(answer)