# Oracle

## 기준에 따라 순위 매기기

### RANK, DENSE_RANK, PARTITION

##### RANK

- `ORACLE`에서는 컬럼의 값을 이용한 순위를 조회할때 `RANK`를 활용한다.

- `RANK()` : 중복 순위 개수만큼 다움 순위 값을 증가 시킴
  
  - `DENSE_RANK()`와 차이점은 아래 이후 참조

- `RANK`함수는 아래와 같이 사용한다.
  
  ```sql
  SELECT NAME, RANK() AS RANK OVER (ORDER BY AMOUNT DESC)
  FROM TABLE1
  ```
  
  `RANK`함수와 같이 사용하는 `OVER`함수 내의 `ORDER BY`로 지정한 컬럼의 값 대로 순위가 매겨지게 된다.

- 위 예시에서 `TABLE1`은 이와 같이 변한다.
  
  | TABLE1 | NAME  | AMOUNT |     | NAME  | AMOUNT | RANK |
  | ------ | ----- | ------ | --- | ----- | ------ | ---- |
  |        | HOSE  | 123    | ->  | JAMES | 10000  | 1    |
  |        | JAMES | 10000  | ->  | HOSE  | 123    | 2    |

##### DENSE_RANK

- `DENSE_RANK()`: 중복 순위가 존재해도 순차적으로 다음 순위 값을 표시한다.
  
  - `RANK()`와 순위를 매긴다는 점에서 같으나, 중복 처리 부분이 다르다.

- 아래 테이블로 차이를 확인하자. `AMOUNT`컬럼을 오름차순으로 `RANK`한다.
  
  | TABLE2 | NAME | AMOUNT |     | NAME | AMOUNT | RANK | DENSE_RANK |
  | ------ | ---- | ------ | --- | ---- | ------ | ---- | ---------- |
  |        | RALO | 3      | ->  | DOPA | 1      | 1    | 1          |
  |        | PAKA | 2      | ->  | PAKA | 2      | 2    | 2          |
  |        | DOPA | 1      | ->  | MEYA | 2      | 2    | 2          |
  |        | MEYA | 2      | ->  | RALO | 3      | 4    | 3          |
  
  `RANK`는 중복 순위에 대한 값을 처리하지만, `DENSE_RANK`는 그렇게 하지 않는다.

##### 그룹별 순위 구하기

- 순위를 그룹화하여 매길때도 있는데, 이때는 `PARTITION BY`절을 추가하여 해당 그룹 내의 순위를 표시한다.

- 예시는 아래와 같다,
  
  ```sql
  SELECT NAME, ADDRESS, AMOUNT, RANK() OVER (PARTITION BY ADDRESS ORDER BY AMOUNT DESC)
  FROM TABLE3
  ORDER BY ADDRESS, AMOUNT 
  ```
  
  `ADDRESS`로 그룹화된 컬럼내에서 `AMOUNT`에 따라 순위가 매겨진다.

- | TABLE3 | NAME | ADDRESS | AMOUNT | RANK |
  | ------ | ---- | ------- | ------ | ---- |
  |        | HOSE | 광주      | 15     | 1    |
  |        | LINA | 광주      | 12     | 2    |
  |        | PAKA | 서울      | 100    | 1    |
  |        | DOPA | 서울      | 50     | 2    |
  |        | RALO | 서울      | 23     | 3    |
  
  위 예시 처럼, 지역별로 분류되어 그룹내에서 `AMOUNT`에 따라 순위가 매겨졌다.

##### 그룹별 최소값, 최대값 구하기

- `KEEP()`함수와 `FIRST`,`LAST` 키워드로 **그룹 내**에 최소값, 최대값을 조회할 수 있다.
  
  - **`DENSE_RANK`** 함수에서만 사용 가능하다.

- ```sql
  SELECT NAME, ADDRESS, AMOUNT, 
         MIN(AMOUNT) KEEP(DENSE_RANK FIRST ORDER BY AMOUNT) OVER(PARTITION BY ADDRESS) AMOUNT_MIN
         MAX(AMOUNT) KEEP(DENSE_RANK LAST ORDER BY AMOUNT) OVER(PARTITION BY ADDRESS) AMOUNT_MAX
  FROM TABLE4
  ORDER BY ADDRESS, AMOUNT
  ```
  
  `AMOUNT` 컬럼옆에는 그룹내의 가장 작은 `AMOUNT`값과 가장 큰 `AMOUNT`이 출력된다.

- | TABLE3 | NAME | ADDRESS | AMOUNT | AMOUNT_MIN | AMOUNT_MAX |
  | ------ | ---- | ------- | ------ | ---------- | ---------- |
  |        | HOSE | 광주      | 15     | 12         | 15         |
  |        | LINA | 광주      | 12     | 12         | 15         |
  |        | PAKA | 서울      | 100    | 53         | 100        |
  |        | DOPA | 서울      | 50     | 53         | 100        |
  |        | RALO | 서울      | 23     | 23         | 100        |

##### EXTRACT()

- `DATE`형식의 값에서 원하는 날짜형식을 뽑아낼수(extract)있다.

- 아래와 같이 사용한다.
  
  - `EXTRACT(DATE_COLUMN FROM DATE_FUNCTION)`
  
  - `DATE_COLUMN`에는 `DATE`형식의 `COLUMN`값을 넣고
  
  - `DATE_FUNCTION`에는 날짜 함수(`YEAR`, `MONTH`,`DAY`, `HOUR`,`MINUTE`, `SECOND`)를 넣는다.

--- 

#### 레퍼런스

> https://school.programmers.co.kr/questions/42834
> 
> https://school.programmers.co.kr/questions/39218
