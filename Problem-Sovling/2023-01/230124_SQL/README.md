# 230124-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 상품 별 오프라인 매출 구하기

- 상품 정보 `PRODUCT` 테이블과 판매량 데이터 `OFFLINE_SALES`를 `JOIN`하여 상품 별 매출액을 출력하라.

- 매출액 기준으로 내림차순, 상품코드 기준 올림차순 출력

#### 풀이과정

- 두개 테이블 `JOIN`해서 푸는거.. 오케이

- 합치고 `(PRODUCT.PRICE*OFFLINE_SALE.SALES_AMOUNT)`를 통해 매출액을 출력했다.
  
  - 근데 오답 왜일까?...

- `OFFLINE_SALES` 테이블을 훑어보니, `PRODUCT_ID`별로 그룹화된게 아니라, 일자별로 연속적으로 기록한 말 그래도 "판매 기록 데이터"였다.

- 그래서 `PRODUCT_ID`로 그룹화한 `OFFLINE_SALE`데이터를 조인 테이블로 생성 후 조인하였다.
  
  ```sql
  SELECT PRODUCT.PRODUCT_CODE,(B.AMOUNT_SUM*PRODUCT.PRICE) AS SALES FROM PRODUCT
  JOIN (
  SELECT PRODUCT_ID,SUM(SALES_AMOUNT) AS AMOUNT_SUM FROM OFFLINE_SALE
  GROUP BY PRODUCT_ID) B ON PRODUCT.PRODUCT_ID = B.PRODUCT_ID
  ORDER BY (B.AMOUNT_SUM*PRODUCT.PRICE) DESC,PRODUCT.PRODUCT_CODE ASC 
  ```

### 오랜 기간 보호한 동물(1)

- 동물 보호소에 들어온 기록인 `ANIMAL_INS`와 입양나간 기록인 `ANIMAL_OUTS`가 있다.

- 아직 입양가지 못한 동물 중 보호를 시작한지 가장 오래된 3마리의 동물의 `NAME`과 `DATETIME`을 출력하라

#### 풀이과정

- 여러 결과중 단 3마리의 동물을 출력하라.. 이게 관건이다

- `LEFT OUTER JOIN`을 통해 보호 기록은 있지만, 입양 기록이 없는 동물을 찾는다.

- 서브쿼리로 하여 `ROWNUM <= 3`인 동물로 해서 맞았으나..
  
  ```sql
  SELECT * FROM (SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME FROM ANIMAL_INS
  LEFT OUTER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
  WHERE ANIMAL_OUTS.ANIMAL_ID IS NULL 
  ORDER BY ANIMAL_INS.DATETIME
  )
  WHERE ROWNUM <= 3
  ```

- `FETCH` 구문을 통해 원하는 갯수의 행을 조회할 수 있다.
  
  ```sql
  SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME FROM ANIMAL_INS
  LEFT OUTER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
  WHERE ANIMAL_OUTS.ANIMAL_ID IS NULL 
  ORDER BY ANIMAL_INS.DATETIME
  FETCH FIRST 3 ROWS ONLY 
  ```

### 성과 및 피드백

#### 성과

##### 행 제한

- 원하는 조건에 따라 행 개수를 제한한다

- 기본 사용 구조는 아래와 같다.
  
  ```sql
  OFFSET 건수 { ROW | ROWS }
  FETCH {FIRST | NEXT} {건수 | 숫자 PERCENT}
  {ROW | ROWS}
  {ONLY | WITH TIES}
  ```

- `OFFSET`을 통해 조회하는 행의 시작 지점(건수)를 지정하고

- `FETCH`로 반환할 행 또는 비율(`PERCENT`)를 지정한다.

- `ONLY`로 지정한 정확한 값만 반환한다.

- `FETCH`와 `NEXT`, `ROW`와 `ROWS`의 기능의 차이는 없다.

- 행 개수의 3%만 반환할때는 
  
  ```sql
  SELECT NAME, ID FROM TABLE
  ORDER BY ID
  FETCH FIRST 3 PERCENT ROWS ONLY;
  ```

- 행 개수를 3부터 3개만 반환한다면
  
  ```sql
  SELECT NAME, ID FROM TABLE
  ORDER BY ID
  OFFSET 3 ROWS FETCH FIRST 3 PERCENT ROWS ONLY;
  ```
  이러면 `ROWNUM`이 3, 4, 5인 값이 반환된다.

#### 피드백

- 데이터 테이블가 어떤 상태인지 잘 확인하자
- 서브쿼리 형성 후 `JOIN`, `JOIN`과정에서 그룹화 및 집계량 추출.. 어떤 방법이 더 효율적일까에 대한 고민

---

#### 레퍼런스

> [[ORACLE] 행 제한 — IT 일기](https://jjoyling.tistory.com/38)
