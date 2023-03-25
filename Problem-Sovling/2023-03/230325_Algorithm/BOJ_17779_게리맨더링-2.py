# 230325 17779 게리맨더링 2
# 격자, 각 구역(칸)은 5개 선거구중하나에 포함
# 선거구는 하나의 구역 포함, 선거구들끼리는 모두 연결
# 5번 선거구 만들고,, 경계선 길이에 따른 사분면으로 1~4선거구가 나뉨
# 격자 변 길이 5<=n<=20
# (20*20)*(20*20) = 400*400 = 160,000*400
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
answer = sys.maxsize
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    result = [0]*5
                    check = [[0]*n for ii in range(n)]
                    # 돌면서
                    # 1,2,3,4번 선거구 번호매기면서,
                    # 5번 경계선 안쪽이면 5번 - 번호마다 조건 다르게 줘야함
                    for r in range(1,n+1):
                        for c in range(1,n+1):
                            idx = 5
                            if 1 <= r < x + d1 and 1 <= c <= y: # 1
                                if c >= -r + x + y:
                                    # result[4] += board[r-1][c-1]
                                    pass
                                else:
                                    # result[0] += board[r-1][c-1]
                                    idx = 1
                            elif 1 <= r <= x+d2 and y < c <= n: # 2
                                if c <= r - x + y:
                                    # result[4] += board[r-1][c-1]
                                    pass
                                else:
                                    # result[1] += board[r-1][c-1]
                                    idx = 2

                            elif x + d1 <= r <= n and 1 <= c < y-d1+d2: # 3
                                if c >= r - x + y - 2*d1:
                                    # result[4] += board[r-1][c-1]
                                    pass
                                else:
                                    # result[2] += board[r-1][c-1]
                                    idx = 3

                            elif x + d2 < r <= n and y - d1 + d2 <= c <=n: # 4
                                if c <= -r + x+y+2*d2:
                                    # result[4] += board[r-1][c-1]
                                    pass
                                else:
                                    # result[3] += board[r-1][c-1]
                                    idx = 4
                            check[r-1][c-1] = idx

                    for r in range(n):
                        for c in range(n):
                            result[check[r][c]-1] += board[r][c]

                    # print(x, y, d1, d2,result,(max(result)-min(result)))
                    # for cc in check:
                    #     print(cc)
                    answer = min(answer,(max(result)-min(result)))

print(answer)
