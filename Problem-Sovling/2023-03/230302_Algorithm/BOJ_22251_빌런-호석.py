# 230302 22251 빌런 호석

# 1 ~ n의 층에
# k자리 수로 표현한다.
# 현재 x 층인 엘베의 led를
# 올바른 숫자(1 ~ n)가 되도록 1 ~ p 개 반전시킬때,
# 가능한 경우의 수 를 구하라.
# 0
#1 2
# 3  => 칸마다 idx
#4 5
# 6

n, k, p, x = map(int,input().split())

ledOfNums = [[1,1,1,0,1,1,1],[0,0,1,0,0,1,0],[1,0,1,1,1,0,1],
             [1,0,1,1,0,1,1],[0,1,1,1,0,1,0],[1,1,0,1,0,1,1],
             [1,1,0,1,1,1,1],[1,0,1,0,0,1,0],[1,1,1,1,1,1,1],
             [1,1,1,1,0,1,1]]
numToNum = [[] for _ in range(10)]

for start in range(10):
    for end in range(10):
        cnt = 0
        for idx in range(7):
            if ledOfNums[start][idx] != ledOfNums[end][idx]:
                cnt += 1
        numToNum[start].append(cnt)
# for ntn in numToNum:
#     print(ntn)

startNumber = [0]*(k)
result = set()

for idx in range(len(str(x))):
    startNumber[k-len(str(x)) + idx] = int(str(x)[idx])

result.add("".join(list(map(str,startNumber))))
for number in range(1,n+1):
    endNumber = [0]*k
    cnt = 0
    for idx in range(len(str(number))):
        endNumber[k-len(str(number)) + idx] = int(str(number)[idx])

    for idx in range(k):
        cnt += numToNum[startNumber[idx]][endNumber[idx]]
        if cnt > p:
            cnt += p
            break

    if cnt <= p:
        # print(number,startNumber,endNumber, cnt, len(result))
        result.add("".join(list(map(str,endNumber))))
print(len(result)-1)