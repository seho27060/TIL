# 230207-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 식품분류별 가장 비싼 식품의 정보 조회하기

- 긱품 정보를 담은 `FOOD_PRODUCT`테이블이 있을때, `CATEGORY`별로
- 가장 비싼 가격의 제품을
- `CATEGORY`, `MAX_PRICE`, `PRODUCT_NAME` 별로 출력하라
- `CATEGORY`는 '과자', '국', '김치', '식용유'인 경우만 출력하며
- `MAX_PRICE` 순으로 출력하라.

#### 풀이과정

- `CATEGORY`별로 최대 가격을 출력하는건 어렵지 않으나...

- 그룹화 과정에서 `PRODUCT_NAME`을 포함시키면 분류별 최대 가격이 출력이 되지 않고, 그게 아니라면 `PRODUCT_NAME`을 출력하지 못한다.

- 그러해서.. 과자, 국, 김치, 식용유인 `CATEGORY`별 그룹화를 통해 최대 가격을 구한 테이블과

- 기존의 테이블을 `JOIN`하여 `PRICE`가 `MAX_PRICE`와 같은 값을 갖는 상품의 정보를 출력했다.

- 풀이는 아래와 같다.
  
  ```sql
  SELECT A.CATEGORY, A.PRICE AS MAX_PRICE, A.PRODUCT_NAME FROM FOOD_PRODUCT A
  JOIN (
    SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE FROM FOOD_PRODUCT
    WHERE CATEGORY = '과자' OR CATEGORY = '국' OR CATEGORY = '김치' OR CATEGORY = '식용유'
    GROUP BY CATEGORY
  ) B ON A.CATEGORY = B.CATEGORY AND A.PRICE = B.MAX_PRICE
  ORDER BY PRICE DESC
  ```
  
  이거 말고도 컬럼의 값에 따른 순위를 매길수 있는 `RANK`함수를 활용하여 풀이가 가능하다!

- `RANK`와 `PARTITION BY`로 그룹화하여 순위를 매긴 방법은 아래와 같다.
  
  ```sql
  select category, price, product_name
  from (
      SELECT category, price, product_name,
             rank () over (partition by category order by price desc) as rank
      from food_product
      where category in ( '과자', '국', '김치', '식용유')
      )
  where rank = 1
  order by price desc;
  ```
  
  일단 그룹화에 `RANK`을 적용한 테이블을 서브 쿼리로 활용하여 `RANK`가 1인 값, 즉 가장 큰 값을 출력한다.

### 성과 및 피드백

#### 성과

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

#### 피드백

- 서브 쿼리와 `JOIN`하여 문제를 해결했지만.. 항상 그렇듯 더 좋은 방법이 있다.

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/42834
