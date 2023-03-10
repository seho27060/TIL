# 230306-BOJ-비슷한 단어

## 비슷한 단어

- https://www.acmicpc.net/problem/2179

- `n <= 20,000`개의 문자열이 주어진다.

- 문자열간 최대 길이의 접두어를 갖는 두개의 문자열을 출력하라.

- 이때 입력 순서에 따라 출력하시오

#### 풀이과정

1. 뭐지 `이진 탐색`인가 했지만, 이러나 저러나 전체 조합에 대해 탐색해야 했다.

2. 다른점이라면 앞의 1글자부터 다른 문자열끼리는 안구해도 된다.
   
   - 문자열을 정렬하면 주위에는 최소한 앞글자는 비슷한 애들끼리 모이게 된다.
   
   - 하지만 입력 순서를 잊지 않아야 하기 때문에 `(input(),indx)`형식으로 입력 문자열들을 저장했다.

3. 정렬된 문자열 `getStr`에서 `i`번째 문자열을 `i+1`번째 문자열부터 비교하면 된다.
   
   - 이때 첫글자가 다르다면 `i`번째 문자열에 대한 비교대상은 없으므로 `break`

4. 한바퀴 돌면서...가장 긴 접두어를 만드는 두개의 문자열을 탐색한다.

5. 이때 주의해야할 점은 출력은 답이 여러개일 시 입력 **순서**에 따라 정렬했을때 가장 먼저나오는 값을 원한다.

6. 따라서 접두어의 최대길이를 갱신하여 `answer`을 새로 구하거나, 접두어의 최대길이와 동일한 경우의 수를 구할 경우 답을 입력 순서에 따라 추가해줘야 한다.
   
   - 이거때문에 많이 헤맸다 ㅎ.. 마지막에 정렬을 잘못해줌
- 다른 풀이로는 접두어를 `key`로 하여 `key-value` 해쉬(딕셔너리)를 활용한 풀이도 있다.

#### 성과 및 피드백

##### 성과

- 성과

##### 피드백

- 정신없이 풀고, 기존의 풀이를 고집하다 보니 오랜시간이 걸렸다 ^^...

#### 레퍼런스

> 