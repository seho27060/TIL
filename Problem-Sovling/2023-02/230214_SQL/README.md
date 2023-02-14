# 230214-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 5월 식품들의 총매출 조회하기

- 식품 테이블 `FOOD_PRODUCT`와 주문 테이블 `FOOD_ORDER`를 활용하여

- 5월에 주문한 식품의 아이디, 이름, 총 매출을 조회하라

- 총매출 내림차순, 아이디 오름차순으로 출력하라

#### 풀이과정

- ```sql
  SELECT B.PRODUCT_ID, B.PRODUCT_NAME, B.PRICE*SUM(A.AMOUNT) AS TOTAL_SALES FROM FOOD_ORDER A
  LEFT OUTER JOIN FOOD_PRODUCT B ON A.PRODUCT_ID = B.PRODUCT_ID
  WHERE TO_CHAR(A.PRODUCE_DATE,'YYYY-MM') = '2022-05'
  GROUP BY B.PRODUCT_ID, B.PRODUCT_NAME, B.PRICE
  ORDER BY TOTAL_SALES DESC, B.PRODUCT_ID
  ```
  
  왜 같은 4레벨이여도 난이도가 다른가

- 전체 테이블 슥 훑어보고 `FOOD_ORDER`를 메인 테이블로 하여 `FOOD_PRODUCT`와 `JOIN`했다. 이때 기준은 `PRODUCT_ID`
  
  - `JOIN` 이후에 `PRODUCT_ID`가 매칭이 안되는 값이 있다.
  
  - `GROUP BY`로 무시되서 그냥 내비둠

- `JOIN` 테이블에서 `WHERE`로 원하는 날짜에 생산된 상품 조건 넣고

- `GROUP BY`로 그룹화했다.

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- `GROUP BY`를 사용할때, 조회가 가능하도록 컬럼을 고려하자.

---

#### 레퍼런스

> 
