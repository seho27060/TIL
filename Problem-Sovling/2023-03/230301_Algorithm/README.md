# 230301-BOJ-불!

## 불!

- https://www.acmicpc.net/problem/4179

- `1 <= r, c <= 1,000` 인 `board`에 

- 길과, 벽, 지훈이와 불이 있다.

- 불은 매분마다 사방으로 확산되고,

- 지훈이는 매분마다 사방 중 한칸으로 이동할 수 있다.

- `board`의 가장 자리에 오면 탈출이 가능하다. 가능한 탈출 경로 중 최소 시간을 출력하라, 없다면 `"IMPOSIBLE"`을 출력

#### 풀이과정

1. `board`의 크기가 좀 애매하긴 한데.. 일단 우선탐색 풀이이다.

2. 근데 지훈이의 탈출경로는 매분마다 확산되는 불에 따라 바뀔 수도 있고..

3. 단순한 `bfs`가 아닌, 이동 중에 확산되는 불의 위치를 고려해야 한다.

4. `백트래킹`을 활용하여 지훈이의 이동경로에 따른 여러 경우의 수를 고려했으나, 범위가 너무 광대해지므로 기각

5. 여러 경우의 수의 이동 중 마지막 이동 위치만을 갱신해주면 된다.
   
   - 불 역시도 마지막에 확산된 자리들만 갱신해준다.

6. 불과 벽을 동일하게 `"#"`로 표현하기로 하고..만약 여러 경우의 수의 지훈이가 가장자리에 오면 결과값을 체크한다.

#### 성과 및 피드백

##### 성과

- ##### 피드백

- 

#### 레퍼런스

> 
