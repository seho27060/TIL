# 230303 9935 문자열 폭발
# 길이 <= 1,000,000 짜리 문자열
# 폭발하는 문자열이 주어지는데,
# 모든 폭발이 끝난 후 문자열을 출력하라

# 스택으로 문자열 쌓고,

getStr = input().rstrip()
boom = input().rstrip()

nxtStr = []

for idx in range(len(getStr)):
    nxtStr.append(getStr[idx])
    if len(nxtStr) >= len(boom):
        if "".join(nxtStr[-len(boom):]) == boom:
            for _ in range(len(boom)):
                nxtStr.pop()

if len(nxtStr) <= 0:
    print("FRULA")
else:
    print("".join(nxtStr))
