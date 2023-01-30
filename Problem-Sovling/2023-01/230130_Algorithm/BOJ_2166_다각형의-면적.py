# 230130 2166 다각형의 면접

#  n < 10,000
# n개 점으로 이뤄진 다각형의 면적구하기?..

import sys

input = sys.stdin.readline

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
points.append(points[0])
answer = 0

for idx in range(n):
    answer += points[idx][0]*points[idx+1][1]
    answer -= points[idx][1]*points[idx+1][0]

print(round(abs(answer)/2,2))