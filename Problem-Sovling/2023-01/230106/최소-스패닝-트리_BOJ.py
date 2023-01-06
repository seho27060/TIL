# 230106 BOJ 1197 최소 스패닝 트리
# 그래프의 최소 스패닝 트리를 구하라
# 모든 정점을 연걸하면서 그 가중치 합이 최소가 되도록
# 정점 = 10,000, 간선 = 100,000
# => 프림..크루스칼..
import heapq
import sys

input = sys.stdin.readline

v, e = map(int,input().split())

graphs = [[] for i in range(v)]
record = set()

for _ in range(e):
    a, b, c = map(int,input().split())
    graphs[a-1].append([c,b-1])
    graphs[b-1].append([c,a-1])

answer = 0

queue = [[0,0]]

while queue:
    if len(record) == v:
        break
    weight, now = heapq.heappop(queue)

    if now not in record:
        record.add(now)
        answer += weight
        for nxt in graphs[now]:
            heapq.heappush(queue,nxt)

# print(result)
print(answer)

