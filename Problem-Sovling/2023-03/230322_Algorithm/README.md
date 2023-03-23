# 230321-BOJ-이차원 배열과 연산

## 이차원 배열과 연산

- https://www.acmicpc.net/problem/17140

- 이차원 배열의 행 개수가 열 개수보다 크거나 작으면 "행 연산"

- 그게 아니라면 "열 연산"할때, 주어진 `r,c`위치의 값이 `k`가 되는 시간을 구하라.

- 연산은 (0,숫자개수),(1,숫자개수),(3,숫자개수),(i,숫자개수) 가 풀어져 `0 0의숫자개수 1 1의숫자개수 3 3의숫자개수 ... i i의숫자개수`의 형식으로 다시 정렬되어 계산된다.

### 풀이과정

1. `while`문으로 시간을 반복하면서 구현... 시간이 100을 초과하면 -1을 초과하도록 조건을 걸어줘야 한다.

2. 연산을 할때, `defaultdict`를 활용하여 숫자마다의 개수를 카운트하고

3. `defaultdict.items()`에 `lambda`를 활용하여 정렬 기준을 선택하여 정렬 진행 후,

4. 행 연산이면 행대로... 열 연산이면 열 대로..하여 새로운 이차원 배열을 반환하여

5. 시간마다 연산에 따른 배열을 갱신했다.

### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 행 연산, 열 연산에서 "연산"이라는 행위가 공통이기 때문에... 분리가 가능할 거같은데..귀찮아서 안함 ㅎ..
- 열 연산의 경우, 행으로 계산을 해서..다시 열로 변환했는데.. 쉽지 않다 다른 방법이 있을거 같다.
- 시간을 나타내는 `answer`이 100을 "초과"하면 `-1`을 반환하는 건데, "이상"으로 조건을 줘서 자꾸 틀림 ㅎ

--- 

#### 레퍼런스

> https://www.acmicpc.net/board/view/42456