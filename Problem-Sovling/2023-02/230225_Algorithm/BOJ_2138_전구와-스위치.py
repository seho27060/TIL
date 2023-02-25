# 230225 2138 전구와 스위치
import copy
# n <= 100,000 개의 전구가 있다. 하나를 선택하여 i-1, i, i+1의 전구 상태가 "뒤 바뀜"
# 원하는 상태를 만들기 위해 최소 몇번 눌러야 하는가...
import sys
n = int(input())

lights1 = list(map(int,list(input())))

lights2 = copy.deepcopy(lights1)
lights2[0] = 1 -lights2[0]
lights2[1] = 1 -lights2[1]
target = list(map(int,list(input())))

result = sys.maxsize

count = 0
for idx in range(1,n):
    if lights1[idx-1] != target[idx-1]:
        count += 1
        for move in range(-1,2):
            if 0 <= idx+move < n:
                lights1[idx+move] = 1 - lights1[idx+move]
if lights1 == target:
    result = min(result,count)
count = 1
for idx in range(1,n):
    if lights2[idx-1] != target[idx-1]:
        count += 1
        for move in range(-1,2):
            if 0 <= idx+move < n:
                lights2[idx+move] = 1 - lights2[idx+move]
if lights2 == target:
    result = min(result,count)
if result >= sys.maxsize:
    result = -1

print(result)
