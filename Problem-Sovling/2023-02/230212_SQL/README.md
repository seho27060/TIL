# 230212-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 보호소에서 중성화한 동물

- 보호소에 온 데이터와 입양간 데이터를 비교하여,

- 들어올때는 중성화가 안됐지만, 입양갈때는 중성화된 동물의

- 아이디, 이름, 종을 출력하라

- 아이디 순으로 정렬 조회

#### 풀이과정

- ```sql
  SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME FROM ANIMAL_OUTS A
  JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
  WHERE B.SEX_UPON_INTAKE LIKE '%Intact%' AND ((A.SEX_UPON_OUTCOME LIKE '%Spayed%') OR (A.SEX_UPON_OUTCOME LIKE '%Neutered%'))
  ORDER BY A.ANIMAL_ID
  ```
  
  어렵지 않다. 입양 나간 `ANIMAL_OUTS` 를 메인 테이블로 두고 보호소에 온 데이터 `ANIMAL_INS`를 서브 테이블로 하여 `JOIN`한다.

- `WHERE`를 통해서  `ANIMAL_INS`에서는 중성화가 안된 상태지만, `ANIMAL_OUTS`에서는 중성화가 된 동물을 찾아 출력한다.
  
  - `LIKE`를 활용하여 문자열비교한다.

### 주문량이 많은 아이스크림을 조회하기

- 상반기 아이스크림 주문 테이블 `FIRST_HALF`와 7월 주문 테이블 `JULY`의 데이터를 활용하여 주문량이 가장 많은 3개의 아이스크림을 조회하라

#### 풀이과정

- ```sql
  SELECT FLAVOR FROM (
      SELECT * FROM FIRST_HALF
      UNION
      SELECT * FROM JULY)
  GROUP BY FLAVOR
  ORDER BY SUM(TOTAL_ORDER) DESC
  FETCH FIRST 3 ROWS ONLY
  ```
  
  `JOIN`으로 분류된 문제인데.. `UNION`으로 풀이했다.

- 뭐 `FIRST_HALF`의 `SHIPMENT_ID`가 `JULY`의 외래키라는 데, 딱히 상관없는 설명같다.

- 두개 테이블을 `UNION`하고 `GROUP BY`로 `FLAVOR`별로 그룹화했다. 그리고 `TOTAL_ORDER`의 합 구하기

- `SUM(TOTAL_ORDER)`대로 내림차순 정렬

- `FETCH` 구문으로 원하는 만큼 조회한다.

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- `UNION`,`FETCH` 사용할때마다 헷갈린다.

---

#### 레퍼런스

> 
