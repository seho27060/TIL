# 230123 2467 용액
# 용액의 수치 리스트가 정렬된 상태로 주어짐
# 두개 용액 더하여 0에 가까운 수를 찾아라.
# -> 두 포인터

import sys

input = sys.stdin.readline

n = int(input())
liquids = list(map(int,input().split()))

start, end = 0, n-1
answer = max(liquids, key=lambda x:abs(x))*2
answerLiquids = [-1,-1]

while start < end:
    result = liquids[start] + liquids[end]
    if abs(answer) > abs(result):
        answer = result
        answerLiquids = [liquids[start],liquids[end]]
    if result < 0:
        start += 1
    elif result > 0:
        end -= 1
    else:
        break
print(*answerLiquids)