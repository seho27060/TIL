# 230223 2110 공유기 설ㅇ치
# 수직선 위 n 개 좌표,.
# 공유기 c개 설치
# 1 2 4 8 9
#  1 2 4 1
# 일단 제일 처음, 제일 끝에 하나씩

import sys

input = sys.stdin.readline

n, c = map(int,input().split())
houses = sorted([int(input()) for _ in range(n)])

# 매개변수, start, end, mid를 공유기 위치간 거리로 고려하기..

start = 1
end = houses[-1]-houses[0]

while start <= end:
    mid = (start+end)//2
    loc = houses[0]

    cnt = 1

    for idx in range(len(houses)):
        if houses[idx] - loc >= mid:
            loc = houses[idx]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        answer = mid
    elif cnt < c:
        end = mid - 1
print(answer)
