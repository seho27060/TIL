# 230307-BOJ-줄세우기

## 줄세우기

- https://www.acmicpc.net/problem/2631

- `n <= 200`의 범위의 `n`개의 숫자가 무작위로 입력된다.

- 모든 숫자를 순서대로 배치하기 위해 옮겨야 하는 최소의 횟수를 구하라.

- 하.. `DP`..

### 풀이과정

1. 각 `i`의 숫자가 `i-1`의 바로뒤에 위치하면서, `i+1`이 그 뒤 어딘가에 위치하는 가 를 보면서 여러 경우의 수로 나누어 풀이할려 했으나.
   
   - `n`이 200이므로 이러한 재귀적 경우의 수 탐색은 오버헤드가 분명하다..

2. 힌트를 보니 `DP`라고 하는데...`LIS` 최장 증가 부분 수열 알고리즘을 활용한다.

3. 주어진 배열 `kids`에서 최장 증가 부분 수열을 구한다.

4. 전체 개수 `n`에서 최장 증가 부분 수열의 길이만큼 빼주면 답이 된다.
   
   - 왜? -> 최장 증가 부분 수열은 어차피 증가하는(= 정렬된) 상태이므로, 나머지 애들만 적절한 자리에 배치해주면
   
   - 최소의 횟수로 모든 아이들을 번호대로 정렬할 수 있다.

5. 이런 쇼킹이 있나

### 성과 및 피드백

#### 성과

##### LIS(Logest Increasing Subsequence,최장 증가 부분 수열)

1. `DP`를 활용한 `O(n^2)` 이 걸리는 방식
   
   ```python
    numbers = list(map(int,input().split()))
    dp = [1]*len(numbers)
   
    for now in range(len(numbers)):
        for nxt in range(now):
            if numbers[now] > numbers[nxt]:
                dp[now] = max(dp[now],dp[nxt]+1)
   ```
   
   - `dp`의 각 `dp[i]`는 `i`번째 숫자보다 작은 수의 개수이다.
   
   - 이중 `for` 구조를 통해 모든 배열을 2번 중첩하여 탐색한다.

2. `이진탐색`을 활용한 `O(nlogn)`이 걸리는 방식
   
   ```python
   def bisecSearch(idx):
       global numbers, dp
   
       start, end = 0, len(dp)
   
       while start < end:
           mid = (start+end)//2
           if dp[mid] >= numbers[idx]:
               start = mid+1
           else:
               end = mid-1
       return start
   
   numbers = list(map(int,input().split()))
   dp = [numbers[0]]
   
   for start in range(len(numbers)):
       if numbers[start] > dp[-1]:
           dp.append(numbers[start])
       else:
           idx = bisecSearch(start)
           dp[idx] = numbers[start]
   ```
   
   - `이진 탐색`를 `bisect` 라이브러리에서 가져와 사용해도 되고 직접 구현해서 사용해도 된다.
   - `dp`는 `numbers`의 가장 첫번째 요소를 갖고 시작하며
   - `start`번째 숫자가 `dp`에 존재하는 요소들 보다 커서 마지막에 추가되거나,
   - 중간에 삽입되거나 를 결정할 수 있다.                      

#### 피드백

- `DP`는 어려워

--- 

#### 레퍼런스

> [가장 긴 증가하는 부분 수열(LIS) 완전 정복 - 백준 파이썬](https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
> 
> https://www.acmicpc.net/problem/2631
