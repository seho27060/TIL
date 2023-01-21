# 230121 BOJ 팰린드롬?

# n개 자연수 수열이 있을때
# m번의 질문으로
# s번째 수부터 e번째 수가 팰린드롬인지 묻는다.
# 그에 대한 대답을 출력하라

# n < 2,000
# m < 1,000,000

# s1. 미리 i부터 j까지 팰린드롬 여부 구하기?
# 검증 시작점 k번째부터 양옆으로 검증
# 팰린드롬은 중심 기준으로 한번이라도 안되면 이 그 이후 다 안됨 (홀수인경우)
#
import sys

input = sys.stdin.readline

def isPalindrome(start,end):
    global numList
    if (end - start + 1) % 2 == 0:
        if end == start:
            sIdx = (end + start) // 2
            eIdx = sIdx
        else:
            sIdx = (end+start)//2
            eIdx = sIdx + 1
    else:
        sIdx = (end + start) // 2
        eIdx = sIdx

    while 1 <= sIdx and eIdx < n:
        # print(sIdx,eIdx)
        if update[sIdx][eIdx]:
            if board[sIdx][eIdx]:
                pass
            else:
                break
        else:
            update[sIdx][eIdx] = 1
            if numList[sIdx] == numList[eIdx]:
                board[sIdx][eIdx] = 1
            else:
                break
        sIdx -= 1
        eIdx += 1

n = int(input())
n += 1
numList = [0]
numList.extend(list(map(int,input().split())))
m = int(input())

board = [[0]*n for _ in range(n)]
update = [[0]*n for _ in range(n)]

for question in range(m):
    s, e = map(int,input().split())
    if update[s][e]:
        print(board[s][e])
    else:
        isPalindrome(s,e)
        print(board[s][e])

