# 230207-BOJ-외판원 순회

## 별자리 만들기

- https://www.acmicpc.net/problem/2098

- `DP`, `비트마스킹`, `DFS`를 혼합하여 풀이해야한다...!

#### 풀이과정

1. `DP`, `비트마스킹`, `DFS`를 활용해야 한다..

2. 주어진 자료가 그래프형식을 띄고 있고, 순환경로를 이룬다.
   
   - `0 - 1 - 2 - 3 - 4 - 0`와 `2 - 3 - 4 - 0 - 1 - 2`은 서로 같은 경로다.

3. 지나간 도시에 대한 기록을 `비트마스킹`으로 해결한다.
   
   - 아래 `비트마스킹`을 정리해놓겠다.
   
   - `0001`, `0101`은 각 1과 5를 나타내고.. 비트 시프트 연산자(`>>`, `<<`)와 비트연산자(논리 연산자,`&`, `|`)를 활용한다.

4. 3.의 지나간 도시에 대한 `비트마스킹`으로 현재위치에서 방문하지 않는 도시를 거쳐 출발점으로 돌아오는 비용을 `DP`로 저장한다.
   
   - `DP[NOW][VISITED]`는 현재는 `NOW` 도시에 있으며 방문현황은 `VISITED`라는 비트마스킹으로 표현된 값(행렬)에 아직 방문하지 않는 도시들을 거쳐 다시 시작점으로 돌아가는 최소 비용이다.

5. 아래의 코드를 보면..
   
   ```python
   minDst = sys.maxsize
       for nxt in range(n):
           if graphs[now][nxt] == 0 or visited & ( 1 << nxt):
               continue
           minDst = min(minDst,dfs(nxt,visited | ( 1 << nxt )) + graphs[now][nxt])
       dp[now][visited] = minDst
   ```
   
   현재 지점에서 다음 지점의 가는 길이 없거나(`graphs[now][nxt] == 0`), 다음 지점을 이미 방문했다면(`visited & (1 << nxt)`) 최소 비용을 연산하지 않는다.
   최소 거리를 연산하는 점화식은 현재 지점에서 방문하지 않은 지점을 모두 방문하고 돌아옴을 표현한다.

#### 성과 및 피드백

##### 비트마스킹

- 코드에서 사용되는 모든 연산자는 결국 비트(이진수)로 표현된 값을 연산한다.

- 기계어에 가깝기 때문에 정수 표현과 같은 자연어에 가까운 자료를 통한 연산보다 빠르고, 적은 메모리를 활용하여 사용할 수 있다.

- 예시는 아래와 같다.
  
  - `0100 & 0111 = 0100`
  
  - `0100 | 1011 = 1111`
  
  - `0100 ^ 0111 = 1000`, 각 비트를 XOR 연산(각 자리 비트가 서로 같으면 1, 다르면 0)
  
  - `0011 <<  2 = 1100`
  
  - `1000 >> 3 = 0001`

#### 레퍼런스

> [[다이나믹 프로그래밍/파이썬] 백준 2098번 : 외판원 순회 / 골드 1](https://yiyj1030.tistory.com/488)
> 
> [[백준] 2098 외판원 순회 (Python 파이썬) :: AndroidTeacher](https://hongcoding.tistory.com/83)
> 
> [[알고리즘] 비트마스킹(bitmasking) 이란 :: 굳건하게](https://travelbeeee.tistory.com/451)