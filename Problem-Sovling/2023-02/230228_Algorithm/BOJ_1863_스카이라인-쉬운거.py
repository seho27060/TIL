# 230228 1863 스카이라인 쉬운거

# x < 1,000,000. y <= 500,000
# 처음에 1,000,000 배열 0으로 초기화
# 받아가면서... 건물 체크
# 스택활용?
# 스택에 건물들 저장.
# 입력받으면 스택 마지막하고 비교.
# 같으면 -> 해당 요소(건물번호,높이)
# 크면 -> (건물번호+1, 높이)
# 작으면 -> 마지막 버려, 반복. 그러다 아무것도 없으면 -> (건물번호 + 1, 높이)
import sys

input = sys.stdin.readline

n = int(input())

stack = [] # (건물번호(idx), 높이) 저장
idx = 0
for building in range(n):
    x, y = map(int,input().split())

    if not stack and y != 0:
        idx += 1
        stack.append((idx,y))
    else:
        while 1 and stack:
            if stack[-1][1] >= y:
                if stack[-1][1] == y:
                    break
                else:
                    stack.pop()
                    if not stack and y != 0:
                        idx += 1
                        stack.append((idx,y))
                        break
            else:
                idx += 1
                stack.append((idx,y))
                break
    # print([x,y],idx,stack)
print(idx)