# 230311 1943 동전 분배
# 동전이 주어지는데
# 윤화와 준희는 돈을 딱 절반으로 나누고 싶다.
# 근데 동전으로 구성되어서 그럴 수도 있고, 아닐 수도 있따.
# 가능한가 아닌가를 출력하라.
# 돈을 10만원 이하로 주어지며, 100번 이하로 제안된다.
# 3*(100,000//2*100) = 15,000,000 의 시간복잡도를 갖는 dp 반복

import sys
from collections import defaultdict

input = sys.stdin.readline

for tc in range(3):
    n = int(input())
    coins = []
    sumCoin = 0
    coinDict = defaultdict(int)
    for _ in range(n):
        value, cnt = map(int,input().split())
        sumCoin += value*cnt
        coins.append(value)
        coinDict[value] += cnt
    coins.sort(reverse=True)
    # print(coinDict)
    result = 0
    if sumCoin%2 == 0:
        dp = [[] for _ in range(((sumCoin//2)+1))]
        dp[0] = defaultdict(int)
        dp[0][0] += 1
        # print(len(dp),dp)
        for money in range(1,(sumCoin//2)+1):
            for coin in coins:
                if money - coin >= 0:
                    # print(money, coin)
                    if dp[money-coin]:
                        coinCnt = dp[money-coin][coin]
                        if coinCnt + 1 <= coinDict[coin]:
                            nxtDict = dp[money-coin].copy()
                            nxtDict[coin] += 1
                            dp[money] = nxtDict
                            # print(dp)
                            break
        # print(dp)
        if dp[sumCoin//2]:
            result += 1

    print(result)


