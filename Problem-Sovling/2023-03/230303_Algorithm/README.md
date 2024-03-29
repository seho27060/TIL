# 230303-BOJ-문자열 폭발

## 문자열 폭발

- https://www.acmicpc.net/problem/9935

- `1,000,000` 보다 작은 길이의 문자열에서

- 길이가 `36`보다 작은 폭발하는 문자열이 있다.

- 폭발 문자열들은 그대로 사라져버리고 나머지 문자열들은 사라진 부분을 제외하고 연결된다.

- 모든 폭발 문자열이 사라진 후 남은 문자열의 형태를 출력하라.

#### 풀이과정

1. `스택`을 활용한 문제는 감 잡았다.

2. 스택을 하나 갖고, `getStr`이라는 입력 문자열을 하나씩 순회한다.
   
   - 시간복잡도 `O(n)`

3. 하나씩 추가하면서, 길이가 `boom`보다 길거나 같으면 폭발 문자열인지 확인한다.
   
   - 시간복잡도 `O(36)`

4. 폭발 문자열이라면 빼버린다.

5. 스택에 남겨진 문자열들은 폭발 문자열이 사라진 이후의 문자열이 되므로.. 정답이 된다.

#### 성과 및 피드백

##### 성과

- 길이가 `n` 문자열 중 마지막 `k` 길이 부분 문자열을 제외하고 **복사**하는 것과
- `pop()`을 `k``번 반복하여 문자열을 **제거**하는 방법중 시간 복잡도는 뭐가 높을까?
  - 복사하는 경우는 아무래도 전체 길이를 순회하기 때문에 `O(n)`이 걸린다.
  - 반복적인 작업이 코드 상으로 확인 가능한 `pop`의 경우 `O(k)`가 걸린다.

##### 피드백

- 코드상으로 보여지는 부분 만으로 알고리즘을 판단하지 말자, 내부적인 작동 방법을 고려하자.

#### 레퍼런스

> https://www.acmicpc.net/board/view/108030
