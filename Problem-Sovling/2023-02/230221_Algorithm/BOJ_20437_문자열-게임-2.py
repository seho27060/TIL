# 230221 20437 문자열 게임 2
# 문자열 w에서 어떤 문자( 길이는 < 10,000 )
# 어떤 문자를 k개 포함하는 가장짧은 연속 문자열의 길이
# 어떤 문자를 k개 포함하고, 문자열의 첫번째와 마지막이 어떤 문자인 가장 긴 연속 문자열의 길이
#를 출력하라

import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for tc in range(t):
    W = input().rstrip()
    K = int(input())
    alpabetDict = defaultdict(list)

    answer = []
    for idx in range(len(W)):
        alpabetDict[W[idx]].append(idx)
        if len(alpabetDict[W[idx]]) >= K:
            answer.append(alpabetDict[W[idx]].copy())
            alpabetDict[W[idx]].pop(0)

    if answer:
        a = min(answer, key=lambda x:x[-1]-x[0])
        b = max(answer, key=lambda x:x[-1]-x[0])

        print(a[-1]-a[0]+1,b[-1]-b[0]+1)
    else:
        print(-1)
