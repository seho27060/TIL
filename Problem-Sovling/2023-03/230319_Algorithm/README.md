# 230319-BOJ-드래곤 커브

## 드래곤 커브

- https://www.acmicpc.net/problem/15685

- 주어진 좌표상에서 주어진 방향으로 시작하여 세대별로 직선을 잇는.."드래곤 커브"라는게 있다.

- 여러 드래곤커브로 `100*100`짜리 격자를 채울때

- 정사각형의 네 변이 모두 칠해진 드래곤 커브에 해당되는 

- 정사각형의 개수를 출력하라.

### 풀이과정

1. 뭐지 싶은 문제..드래곤 커브를 이해를 하긴하겠는데 어떻게 이제까지 지나온 길을 마지막 끝점을 기준으로 90도 돌린다는...?

2. 직접 그려보니 규칙이 나온다..(a,b)의 방향으로 이제까지 이동했다면,
   
   - `[우, 상, 좌, 하]`로 이뤄진 이동 방향 배열이 있을때, `(a,b)`는 각 방향의 어떤 인덱스라 할때,
   
   - `(b+1,a+1)`는 마지막 끝점에서 다음 이동 방향이다.

3. 그리고 주의해야 할 점이
   
   - 세대 `g`는 해당 드래곤 커브가 몇 세대까지 생성되느냐 이고,
   
   - `x,y` 좌표들이 각각 가로 선인지, 세로 선인지 잘 구분해야 한다.

4. 다..그렇게 구현하고 마지막에 드래곤 커브들이 지나간 자리로 만들어지는 정사각형의 개수를 구한다.

### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 피드백

--- 

#### 레퍼런스

> 
