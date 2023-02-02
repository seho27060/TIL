# 230202 14003 가장 긴 증가하는 부분 수열 5
# n < 1,000,000
# -1,000,000,000 <= a <= 1,000,000,000...
# dp + "역추적"!!!!

import sys
from collections import deque

def binarySearch(lst,number):

    start, end = 0, len(lst)-1

    while start <= end < len(lst):
        mid =(start+end)//2

        if lst[mid] < number:
            start = mid+1
            if number <= lst[mid+1]:
                return mid+1
        else:
            end = mid-1
    return -1
input = sys.stdin.readline

n = int(input())
nums = deque(list(map(int,input().split())))

dp = [-float("inf")]
idxForReverse = [(-float("inf"),0)]

while nums:
    num = nums.popleft()

    if num > dp[-1]:
        idxForReverse.append((num,len(dp)))
        dp.append(num)
    else:
        result = binarySearch(dp,num)
        dp[result] = num
        idxForReverse.append((num,result))

doLen = len(dp)-1
answer = []

while idxForReverse and doLen:
    num, idx = idxForReverse.pop()
    if idx == doLen:
        answer.append(num)
        doLen -= 1

print(len(answer))
print(*answer[::-1])