# 230218-BOJ-감시 피하기

## 감시 피하기

- https://www.acmicpc.net/problem/18428

- 바쁘다바뻐 현대사회에서 쉬어가는 날도 있는 거잖아요.

#### 풀이과정

1. `n*n <=36`인 `board`에 빈공간, 학생, 선생, 장애물이 놓여져있다.

2. 선생님이 상하좌우 일직선으로 감시하여 학생을 감지하면 fail

3. 장애물을 단 3개만 놓아서 학생들이 선생들의 감시를 피할 수 있는지를 출력하는 구현문제

4. `combinations`로 가능한 경우의 수를 모두 만들고(36C3) board에 3개의 새로운 장애물을 배치하고 탐색함.

#### 성과 및 피드백

##### 성과

##### 피드백

- 

#### 레퍼런스

> 