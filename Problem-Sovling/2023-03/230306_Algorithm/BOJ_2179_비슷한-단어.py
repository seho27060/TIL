# 230306 2179 비슷한 단어
# n <= 20,000개 문자열이 입력되는데
# 그 중 두개의 접두어가 가장 긴 경우 두개 문자열을 출력하라.
# 동일 길이의 최대 길이 접두어가 많다면 앞에 입력된 순서로 출력

# 모든 idx로 부터 해서..
# (문자열, idx) 로 구성
# 문자열 기준으로 정렬
# j번째 애부터 앞글자가 같은 애끼리 비교
# 다르면 break
# idx 부터 마지막까지
import sys

input = sys.stdin.readline

n = int(input())

getStr = [(input().rstrip(),idx) for idx in range(n)]
answer = [[getStr[0],getStr[1]]]
getStr.sort(key=lambda x:x[0])
# print(getStr)

resultLen = -1
for start in range(n):
    result = ""
    startStr = getStr[start]
    resultEnd = -1
    for end in range(start+1,n):
        endStr = getStr[end]

        if startStr[0][0] == endStr[0][0]:
            prefixStr = ""

            for idx in range(min(len(startStr[0]),len(endStr[0]))):
                if startStr[0][idx] == endStr[0][idx]:
                    prefixStr += startStr[0][idx]
                else:
                    break
            if len(result) < len(prefixStr):
                result = prefixStr
                resultEnd = getStr[end]
            elif len(result) == len(prefixStr):
                resultEnd = min(resultEnd,getStr[end], key=lambda x:x[1])
        else:
            break
    if resultEnd != -1:
        if resultLen < len(result):
            answer = [sorted([startStr,resultEnd],key=lambda x:x[1])]
            resultLen = len(result)
        elif resultLen == len(result):
            answer.append(sorted([startStr,resultEnd],key=lambda x:x[1]))
    # print(result,answer)
answer.sort(key=lambda x:(x[0][1],x[1][1]))
# print(answer)
# print(answer)
print(answer[0][0][0])
print(answer[0][1][0])