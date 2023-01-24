# 230124-BOJ-문제집

## 문제집

- https://www.acmicpc.net/problem/1766

- `위상정렬`에 `우선순위 큐`를 활용하여 정렬된 값을 출력하는 문제

- 모든 문제를 다 풀어야(순회해야 할때), 문제마다의 우선순위가 있다.

- 이때 쉬운(번호가 낮은) 문제부터 풀면서 문제마다의 우선 순위를 지키는 값을 출력하라.

#### 풀이과정

1. 문제 읽고 도저히 감을 못잡아서 힌트봄!

2. `위상 정렬`과 `우선순위 큐(heapq)`를 활용한다.

3. `m`개의 문제 우선순위를 받으면서 `i`번 문제의 직접 연결된 자식을 의미하는 `problem`에 추가하고, 자식 노드의 상위에 연결된 노드 개수를 의미하는 `relation`에 1을 추가한다.
   
   ```python
   n, m = map(int,input().split())
   relation = [0 for i in range(n+1)]
   problems = [[] for _ in range(n+1)]
   for _ in range(m):
    a, b = map(int,input().split())
    problems[a].append(b)
    relation[b] += 1
   ```

4. 이후 정렬에 들어간다 이때 사용하는 `queue`는 우선 순위 큐(`heapq`)를 활용하여 인자간 우선순위(문제 번호의 올림차순)에 따라 다음 이동을 고려한다.
   
   ```python
   def polygySort():
    global n, m, relation, problems
    result = []
    queue = []
   
    for s in range(1,n+1):
        if relation[s] == 0:
            heappush(queue,s)
   
    while queue:
        now = heappop(queue)
        result.append(now)
   
        for nxt in problems[now]:
            relation[nxt] -= 1
            if relation[nxt] == 0:
                heappush(queue,nxt)
   ```

5. 위상정렬 템플릿에서 `queue`를 `heapq`로 바꾼거 말곤 다른게 없다.

#### 성과 및 피드백

- 1개의 board를 사용하는게 아닌 각 인자의 차수를 의미하는 다른 board를 사용하는... 공통 board가 두개를 활용하는 문제.

##### 위상 정렬(Topological sort)

- 사이클이 없는 방향 그래프(DAG, directed acyclic graph)의 **모든 노드를 방향성**에 거스르지 않도록 순서대로 나열하는 것.

- 진입차수와 진출차수
  
  - 진입차수(Indegree) : 특정 노드로 들어오는 간선의 개수
  
  - 진출차수(Outdegree) : 특정 노드에서 나가는 간선의 개수

- 위상 정렬 알고리즘
  
  1. 진입차수가 0인 모든 노드를 큐에 넣는다.
     
     - 트리로 생각하면 가장 상위에 있는 노드들(부모가 없는)
  
  2. 큐가 빌 때까지 아래 과정을 반복
     
     1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
        
        - 과정중에 큐의 원소의 노드에 진입차수를 -1
     
     2. 새롭게 진입차수가 0이된 노드를 큐에 넣는다.
        
        - 이전에서 진입차수가 -1되면서 0이 되는 노드가 생김
  - 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.
  
  

---

#### 레퍼런스

> [[이것이 코딩 테스트다 with Python] 36강 위상 정렬](https://freedeveloper.tistory.com/390)
