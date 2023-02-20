# 23020 20055 컨베이어 벨트 위의 로봇
# n 칸짜리 컨베이어 벨트에 로봇을 옮기는데 몇단계에서 0인 칸이 k개이상이 되는지 출력

import sys

input = sys.stdin.readline

n, k = map(int,input().split())
belts = list(map(int,input().split()))
belts.append(0)
robotOnBelts = [0]*n
robotOnBelts.append(0)
answer = 0
# print(belts)
# print(robotOnBelts)
while 1:

    answer += 1
    # 1
    belts[1:] = belts[:2*n]
    belts[0] = belts[-1]
    belts[-1] = 0
    robotOnBelts[1:] = robotOnBelts[:n]
    robotOnBelts[-1] = 0
    robotOnBelts[0] = 0
    # 2
    for idx in range(n-1,-1,-1):
        if robotOnBelts[idx] == 1:
            if idx == n-1:
                robotOnBelts[idx] = 0
            else:
                if robotOnBelts[idx+1] == 0 and belts[idx+1] != 0:
                    robotOnBelts[idx+1] = robotOnBelts[idx]
                    robotOnBelts[idx] = 0
                    belts[idx+1] -= 1
    # 3
    if belts[0] != 0:
        belts[0] -= 1
        robotOnBelts[0] = 1

    # 4
    result = 0
    for idx in range(2*n):
        if belts[idx] == 0:
            result += 1

    # print(answer)
    # print(belts)
    # print(robotOnBelts)
    if result >= k:
        break

print(answer)