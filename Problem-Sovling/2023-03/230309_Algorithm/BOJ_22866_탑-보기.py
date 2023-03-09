# 230309 22866 탑 보기
# idx <= 100,000에 있는 건물이 양쪽으로 보이는 다른 건물의 개수와 가장 가까운 건물 번호 출력

import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int,input().split()))

# 왼쪽부터 stack으로 보이는 건물 찾기
# 오른쪽부터 stack으로 보이는 건물 찾기
# 각 idx에 도착하면 보이는 건물들 입력
# n*2
answer = [[] for _ in range(n)]
stack = []
nearestBuilding = [sys.maxsize]*n
buildingCount = [0]*n

for idx in range(n):
    building = buildings[idx]
    while stack and stack[-1][1] <= building:
        candidate = stack.pop()

    if stack:
        buildingCount[idx] += len(stack)
        nearestBuilding[idx] = min(nearestBuilding[idx],stack[-1][0],key=lambda x:abs(x-idx))
    stack.append([idx,building])

stack = []

for idx in range(n-1,-1,-1):
    building = buildings[idx]
    while stack and stack[-1][1] <= building:
        candidate = stack.pop()
    if stack:
        buildingCount[idx] += len(stack)
        nearestBuilding[idx] = min(nearestBuilding[idx], stack[-1][0], key=lambda x: abs(x - idx))
    stack.append([idx,building])

# 여기서 오버헤드 발생
# 굳이 다 계산해논거에 min안해도 됨
# 계산하면서 건물개수, 가까운 건물 구할수 있네
# 어차피 스택이면 마지막 요소가 가장 가까운거니까..
for idx in range(len(answer)):
    print(buildingCount[idx], end=" ")
    if nearestBuilding[idx] < sys.maxsize:
        print(nearestBuilding[idx]+1)
    else:
        print()

# 휴.. 이게 골드3 적당하지 했다가 된통 뚜드려맞았네