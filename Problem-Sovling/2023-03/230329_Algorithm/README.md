# 230329-BOJ-약수들의 합

## 약수들의 합

- https://www.acmicpc.net/problem/9506

- `n`이라는 숫자의 약수 중 `n`을 제외한 값들의 합이 `n`과 같을 때, "완전수"라고 한다.

- 주어진 `n`이 완전수인지 아닌지 판단하라.

### 풀이과정

1. 주어진 `n`에 대해 약수 구해야함
   
   - `n`의 제곱근 + 1 만큼의 수에 대해 `n %idx`가 0인 `idx`를 찾음
   
   - 찾으면 `HashSet`이라는 집합에 `num/idx`와 `idx` 저장.

2. 약수들을 다 찾고 그 합에 `n`을 뺀 값이 `n`과 동일한지 확인
   
   - `HashSet` 의 값들의 합을 구하는건 `stream` 의 메서드를 사용함.

3. 같다면 `HashSet` 을 정렬하여 요구하는 대로 출력

4. 아니라면 아니라고 출력.

### 성과 및 피드백

#### 성과

- 집합 자료형 `HashSet`, `ArrayList`랑 사용법 비슷함.

- `Stream API`를 활용한..원하는 작업 수행
  
  - 정렬, 합 구하기 등등등..

#### 피드백

- 

--- 

#### 레퍼런스

> 