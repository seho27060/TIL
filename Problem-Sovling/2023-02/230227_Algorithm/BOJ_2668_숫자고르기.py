# 230227 2668 숫자고르기
# 윗칸에는 1 ~ n이 정렬됨
# 아랫칸에는 1 ~ n이 무작위로 배치

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

numbers = [int(input()) for _ in range(n)]
numbers.insert(0,0)
result = []
answer = []
for idx in range(1,n+1):
    comA = set()
    comB = set()

    comA.add(idx)
    queue = deque([idx])

    while queue:
        now = queue.popleft()
        comA.add(now)
        nxt = numbers[now]
        comB.add(nxt)
        if nxt not in comA:
            queue.append(nxt)
            
    if comA == comB and comA not in result:
        result.append(comA)
        answer.extend(comA)
answer = sorted(answer)

print(len(answer))
for ans in answer:
    print(ans)