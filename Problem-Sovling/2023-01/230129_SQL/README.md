# 230129-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 오랜 기간 보호한 동물(2)

- 입양을 간 동물 중
- 보호기간이 가장 긴 
- 동물 2마리의
- `ANIMAL_ID`와 `NAME`을 출력하라

#### 풀이과정

- `INNER JOIN`으로 `ANIMAL_INS`와 `ANIMAL_OUTS`를 `ANIMAL_ID`를 기준으로 JOIN한다.
  
  - 입양을 기록이 없는 행은 삭제된다.

- `ANIMAL_OUTS.DATETIME`와 `ANIMAL_INS.DATETIME`의 차이를 내림차순으로 정렬한 후

- `FETCH _ 숫자 ROWS ONLY`구문으로 원하는 개수의 결과만 출력한다.

- ```sql
  SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME FROM ANIMAL_INS
  JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
  ORDER BY ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME DESC
  FETCH FIRST 2 ROWS ONLY
  ```

### 카테고리 별 상품 개수 구하기

-  상품목록 테이블  `PRODUCT` 에서  `PRODUCT_CODE`의 앞 2자리는 상품의 카테고리이다.
- 카테고리별 상품의 개수를 카테고리 코드 기준 오름차순으로 출력하라.

#### 풀이과정

- 풀다가...`SUBSTR`이란 구문이 있을까?...하다가 있었다 ㅎ..

- `PRODUCT_CODE`를 앞에 2개만 잘라 카테고리 코드로 만들고

- 카테고리 코드로 그룹화하고 정렬했다.

- `COUNT(PRODUCT_ID)`로 카테고리별 상품의 개수를 집계했다.

- ```sql
  SELECT SUBSTR(PRODUCT_CODE,0,2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS FROM PRODUCT
  GROUP BY SUBSTR(PRODUCT_CODE,0,2)
  ORDER BY SUBSTR(PRODUCT_CODE,0,2)
  ```

### 조건별로 분류하여 주문상태 출력하기

- 5월 1일을 기준으로 주문 목록 테이블 `FOOD_ORDER`  의 출고상태를 출력하라.
- `ORDER_ID` 를 기준으로 오름차순 정렬하여 출력한다.

#### 풀이과정

- `CASE WHEN _ THEN _ END` 구문으로 풀이했다..

- `2022-05-01`을 기준으로 작거나 같으면 "출고완료", 크면 "출고대기",  `NULL` 값이라면 "출고미정"으로 출력한다.

### 성과 및 피드백

#### 성과

##### SUBSTR

- 문자열을 자를때 사용하는 함수이다.

- `SUBSTR(컬럼, 시작위치, 길이)` 로 사용한다.

- ```sql
  # ABCDEF, XYZ123 이라는 데이터가 있다고 할때
  SELECT SUBSTR(COLUMN,1, 3), SUBSTR(COLUMN,4,6) FROM TABLE
  # [ABC,XYZ], [DEF,123]이 각각 출력된다.
  ```

#### 피드백

- `FETCH`구문이나 `CASE WHEN`구문을 사용할때 정확한 키워드를 몰라 이전에 배운걸 찾아보게 된다 ㅠ.. 익숙해지도록 하자

---

#### 레퍼런스

> [[ORACLE] 행 제한 — IT 일기](https://jjoyling.tistory.com/38)
