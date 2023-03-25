# 230324-BOJ-연구소 3

## 연구소 3

- https://www.acmicpc.net/problem/17142

- 활성화 바이러스를 "놓을 수 있는" 자리가 `m, 1<=m<=10`개 있을때

- 전체 격자에 바이러스를 활성화 시키는 최소 시간 출력하라.

### 풀이과정

1. 바이러스가 "있는 것"(비활성)과 "놓을 수 있는"(활성)을 구분해야 한다...

2. 구현 방식은 뭐 `BFS`로 재귀나 사이클로해서 1초마다 범위 확장하는 방식이나

3. 각 자리에 바이러스가 닿게 되는 시간으로 채우면 되는데...

4. 빈칸과 비활성 바이러스를 구분해야하는게..좀 어려웠다.

5. 근데 그냥 처음에 빈칸 개수 세고, 바이러스 채워나갈때마다 채워진 개수 count함 ㅎ

6. 그러고 채운 개수 `resultCnt`가 `checkCnt`보다 크거나 같으면 전체 격자가 다 채워졌는지 확인함.

### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 이왜골3?

--- 

#### 레퍼런스

> 