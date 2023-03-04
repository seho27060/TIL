# 230304-BOJ-List of Unique Numbers

## List of Unique Numbers

- https://www.acmicpc.net/problem/13144

- ` n <= 100,000`인 길이를 갖는 수열에서

- 중복되지 않는 수로 이뤄진 부분 수열의 경우의 수를 구하라.

#### 풀이과정

1. `이진 탐색`?..이라고 생각은 했으나, 풀이로 연결은 못했다.

2. 정확한 분류는 `두 포인터` 문제이다.

3. 모든 요소를 시작점으로하여 `start`를 설정한다.

4. `dp`를 활용하여 중복되는 숫자가 있는지 확인한다.

5. `1 2 3` 이라면, `1`, `1 2` `1 2 3`으로 3개가 추가되고
   
   - 시작점은 `2`부터하여 `2`, `2 3` 으로 2개가 추가된다.

#### 성과 및 피드백

##### 성과

- 성과

##### 피드백

- 프대박

#### 레퍼런스

> https://velog.io/@kakasi18/Two-Pointers-Boj13144-List-of-Unique-Numbers
> 
> [[ 13144 ] [ Two-Pointer ] List of Unique Numbers :: 그냥 코딩하는 사람의 블로그](https://nbalance97.tistory.com/204)
> 
> [백준 13144 List of Unique Numbers 파이썬 주석 설명 O](https://77dptjd.tistory.com/27)
