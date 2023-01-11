# 23011 BOJ 1806 부분합
# 연속된 수들의 부분합 중에서 그 합이 S이상이 되는 것 중,
# 가장 짧은 것의 길이를 구하라.

# n <= 100,000, s <= 100,000,000

# index i 부터 합하면서.. 합이 s넘으면 index i부터 다시 빼기..
# 빼면서 s이상이면 계속 길이 갱신하고
# index j에서 s미만되면 거기 기억하고 다시 현재 index부터 부분합 진행
# 위 과정 반복..
# O(n) = ?

import sys

input = sys.stdin.readline

n, s = map(int,input().split())
lst = list(map(int,input().split()))

answer = n+1
result = [0,0]

for i in range(n):
    result[1] += lst[i]
    while result[1] >= s and result[0] <= i:
        answer = min(answer, i + 1 - result[0])
        result[1] -= lst[result[0]]
        result[0] += 1
if answer >= n+1:
    answer = 0
# print(lst)
# print(answer, result)
print(answer)


