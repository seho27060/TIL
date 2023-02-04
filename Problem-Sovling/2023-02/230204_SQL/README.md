# 230204-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 오프라인/온라인 판매 데이터 통합하기

- 온라인 판매 정보 `ONLINE_SALE`과 오프라인 판매 정보 `OFFLINE_SALE` 두개 테이블이 있을때
- 2022년 3월의 판매 데이터의
- 날짜, 상품ID, 유저ID, 판매량을 출력하라.

#### 풀이과정

- 어.. 통합하라 `JOIN`문제인가?,... 싶었는데 아니다. 테이블을 **수직**방향으로, 위아래로 합쳐서 결과를 출력해야한다.

- 무슨 쿼리를 써야하나^^.. `JOIN`은 수평 통합이고, 좌우로 테이블을 이어붙이는건데..

- 하다가 `UNION`이라는 구문을 알게되었다. 테이블을 수직방향을 붙여 출력한다.

- 근데 또 `OFFLINE_SALE`에는 유저ID,`USER_ID` 컬럼이 없다!
  
  - `NULL USER_ID`를 출력문에 할당하면 `NULL`값을 갖는 컬럼으로 출력가능하다.

- 날짜는 `TO_CHAR`로 찾고..`ORDER BY`로 원하는대로 정렬 후 출력

- ```sql
  SELECT TO_CHAR(SALES_DATE,'YYYY-MM-DD') AS SALES_DATE,PRODUCT_ID,USER_ID, SALES_AMOUNT FROM ONLINE_SALE
  WHERE TO_CHAR(SALES_DATE,'YYYY-MM') = '2022-03'
  
  UNION
  
  SELECT TO_CHAR(SALES_DATE,'YYYY-MM-DD') AS SALES_DATE,PRODUCT_ID, NULL USER_ID,SALES_AMOUNT FROM OFFLINE_SALE
  WHERE TO_CHAR(SALES_DATE,'YYYY-MM') = '2022-03'
  
  ORDER BY SALES_DATE, PRODUCT_ID,USER_ID
  ```
  
  각 테이블에서 원하는 날짜를 찾은 후, 병합을 진행했다.
  
  각 테이블의 컬럼이 모두 동일한게 아니니, 공통되는 컬럼으로 `SELECT`를 출력한다.
  
  `USER_ID`는 없으니 `NULL USER_ID`로 전체가 `NULL`인 값으로 출력하도록 한다.

### 성과 및 피드백

#### 성과

##### UNION

- 여러개의 `SELECT`문의 결과를 합치기 위한 구문

- **주의점** 
  
  - 수직으로 붙일때는 **"공통된 컬럼"** 출력하도록 한다. 
  - `ORDER BY`로 인한 정렬은 `UNION`으로 생성한 합집합의 컬럼을 사용한다.

- `UNION`: 각 쿼리의 결과 합을 반환하는 합집합(중복 제거)

- | TABLE1 | NAME  | AMOUNT | TABLE2 | NAME  | AMOUNT |
  | ------ | ----- | ------ | ------ | ----- | ------ |
  |        | HOSE  | 10     |        | LINA  | 40     |
  |        | JAMES | 20     |        | HOSE  | 10     |
  |        |       |        |        | JAMES | 20     |
  
  위와 같은 테이블은 `NAME`, `AMOUNT`로 공통되는 컬럼을 갖는다. 이를 `UNION`을 통해 1개 테이블로 출력한다.

- ```sql
  SELECT NAME, AMOUNT FROM TABLE1 WHERE NAME = 'JAMES'
  UNION
  SELECT NAME, AMOUNT FROM TABLE2 WHERE AMOUNT >= 10
  ```
  
  위 쿼리 결과로 아래와 같은 값을 갖는다. 두 테이블에 `NAME`이 "JAMES"인 행이 겹치지만 중복없이 출력한다.
  
  | RESULT | NAME  | AMOUNT |
  | ------ | ----- | ------ |
  |        | LINA  | 40     |
  |        | HOSE  | 10     |
  |        | JAMES | 20     |

##### UNION ALL

- `UNION ALL` : 각 쿼리의 모든 결과를 포함한 합집합(중복 제거 안함)

- `UNION`의 예시를 조금만 바꿔보자
  
  ```sql
  SELECT NAME, AMOUNT FROM TABLE1 WHERE NAME = 'JAMES'
  UNION ALL
  SELECT NAME, AMOUNT FROM TABLE2 WHERE AMOUNT >= 10
  ```
  
  결과는 아래와 같다. 조건에 해당되지만 두개 테이블에 중복되는 행인 `JAMES`의 결과가 중복되어 나타난다.
  
  | RESULT | NAME  | AMOUNT |
  | ------ | ----- | ------ |
  |        | JAMES | 20     |
  |        | LINA  | 40     |
  |        | HOSE  | 10     |
  |        | JAMES | 20     |

##### NULL COLUMN_NAME

- 위 `UNION`을 출력할때, `TABLE1`에는 컬럼 `ADRESS`가 있지만, `TABLE2`에는 `ADRESS`가 없다. 하지만 `UNION`을 통한 출력은 `NAME`, `AMOUNT`, `ADRESS`하고 싶을때 사용한다.

- ```sql
  SELECT NAME, AMOUNT,ADRESS FROM TABLE1
  UNION
  SELECT NAME, AMOUNT, NULL ADRESS FROM TABLE2
  ```
  
  위와 같이 출력할 경우, `TABLE2`에는 `ADRESSS` 컬럼이 없지만 모든 값이 `NULL`인 가상의 컬럼을 출력한다.

#### 피드백

- `UNION` 사용법

---

#### 레퍼런스

> [[Oracle] 오라클 UNION, UNION ALL 사용법 (쿼리 결과 합치기)](https://gent.tistory.com/383)
