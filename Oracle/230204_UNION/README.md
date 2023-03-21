# Oracle

## 열 기준으로 테이블 합치기

### UNION, UNION ALL

#### UNION

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

#### UNION ALL

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

#### NULL COLUMN_NAME

- 위 `UNION`을 출력할때, `TABLE1`에는 컬럼 `ADRESS`가 있지만, `TABLE2`에는 `ADRESS`가 없다. 하지만 `UNION`을 통한 출력은 `NAME`, `AMOUNT`, `ADRESS`하고 싶을때 사용한다.

- ```sql
  SELECT NAME, AMOUNT,ADRESS FROM TABLE1
  UNION
  SELECT NAME, AMOUNT, NULL ADRESS FROM TABLE2
  ```
  
  위와 같이 출력할 경우, `TABLE2`에는 `ADRESSS` 컬럼이 없지만 모든 값이 `NULL`인 가상의 컬럼을 출력한다.

---

#### 레퍼런스

> [[Oracle] 오라클 UNION, UNION ALL 사용법 (쿼리 결과 합치기)](https://gent.tistory.com/383)
