# 230308 14658 하늘에서 별똥별이 빗발친다
# n*m <= 500,000*500,000인 땅에 별똥별이 내린다.
# l*l <= 100,000*100,000 인 트랜펌린으로 k(<=100)개의 별똥별을 튕겨낼때
# 지구에 부딪히는 별똥별의 개수를 구하라

import sys

input = sys.stdin.readline

n, m, l, k = map(int,input().split())

shootingStars = [list(map(int,input().split())) for _ in range(k)]
# shootingStars.sort()

trampoline = [[l,l],[-l,l],[-l,-l],[l,-l]]

answer = 0

for now in range(k):
    nowStar = shootingStars[now]
    for nxt in range(k):
        nxtStar = shootingStars[nxt]

        x = nowStar[0]
        y = nxtStar[1]
        uX = x + l
        uY = y + l

        starCnt = 0

        for star in shootingStars:
            if x <= star[0] <= uX and y <= star[1] <= uY:
                starCnt += 1

        answer = max(answer,starCnt)
print(k-answer)
