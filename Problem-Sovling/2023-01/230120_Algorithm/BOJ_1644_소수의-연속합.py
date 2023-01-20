# 230119 1644 소수의 연속합
# n <4,000,000
# -> O(n) or O(nlog(n))

import sys

input = sys.stdin.readline

n = int(input())

primeNums = []

for num in range(2,n+1):
    cnt = 0
    for div in range(1,int((num**0.5))+1):
        if num%div == 0:
            cnt += 1
        if cnt >= 2:
            break
    if cnt <= 1:
        primeNums.append(num)
# print(primeNums)

start, end = 0,0
answer = 0
while start <= end < len(primeNums):
    # print(start,end)
    result = sum(primeNums[start:end+1])
    if result == n:
        answer += 1
    if result < n:
        end += 1
    else:
        start += 1
print(answer)