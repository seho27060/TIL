#230310 24337 가희와 탑
# 일직선 상 n개의 건물
# 가희는 idx 0, 다희는 idx n
# 가희가 1번건물을 바라볼때, k번건물이 그 왼쪽 건물들 모다 높으면 가희는 k번건물 볼 수 있음
# 단비(다희가 아니라 단비임 ㅎ)는 n번 건물을 바라볼때 어쩌고 위랑 같은 조건
# 건물개수 n 가희가 볼수있는건물 a개, 단비가 볼수있는건물 b개가 주어지면
# 가능한 건물 높이 정보를 출력하라??
# 건물들 높이가 모두 다를 필요는 없음
# n <= 100,000

n, a, b = map(int,input().split())

highestBuilding = max(a,b)

answer = []


for building in range(1,a):
    answer.append(building)
# print("A",answer)

answer.append(highestBuilding)
# print("High",answer)

for building in range(b-1,0,-1):
    answer.append(building)
# print("B",answer)
# 6 1 1
stack = []
for idx in range(len(answer)+1):
    if stack:
        if len(stack) == a or stack[-1] == 1:
            for mid in range(n-(a+b)+1):
                answer.insert(idx,1)
            break
        if stack[-1] < answer[idx]:
            stack.append(answer[idx])
    else:
        stack.append(answer[idx])
# print(answer)
if len(answer) == n:
    for ans in answer:
        print(ans,end=" ")
else:
    print(-1)