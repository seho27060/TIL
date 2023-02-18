# 230218-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 대여 기록이 존재하는 자동차 리스트 구하기

- 차 대여 기록 테이블에서 대여 시작 날짜가 10월인 

- 차 종류가 "세단"인

- 차의 `CAR_ID`를 내림차순으로 출력하라

#### 풀이과정

- ```sql
  SELECT A.CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
  JOIN CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID = B.CAR_ID AND B.CAR_TYPE = '세단' AND TO_CHAR(START_DATE,'MM') = '10'
  GROUP BY A.CAR_ID
  ORDER BY A.CAR_ID DESC
  ```
  
  테이블 2개를 `JOIN`하여 풀이한다.

- `JOIN` 테이블에서 차 대여 기록 테이블의 `CAR_ID`와 차 종류 테이블의 `CAR_ID`를 기준으로 묶는다.

- 그와 동시에 대여 기록에서 `START_DATE`가 10월인 기록과

- `CAR_TYPE`이 "세단"인 차량을 조건에 할당한다.

- 이후 `CAR_ID`를 기준으로 `GROUP BY`하여

- 내림차순으로 정렬하여 출력

### 성과 및 피드백

#### 성과

##### 

#### 피드백

---

#### 레퍼런스

> 
