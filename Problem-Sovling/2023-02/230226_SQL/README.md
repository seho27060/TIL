# 230226-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 자동차 대여 기록 별 대여 금액 구하기

- 차 대여 기록, 차 종류, 종류 별 할인 정책 3개 테이블을 활용하는 문제.

- 대여 기록 테이블에서 `CAR_TYPE`이 '트럭'이고, 대여 일수에 따른 할인 정책이 적용된 비용을 내림차순, `CAR_ID` 내림차순으로 출력하라.

#### 풀이과정

- ```sql
  SELECT C.HISTORY_ID, 
         C.DAILY_FEE*C.DAYS*(100-NVL(D.DISCOUNT_RATE,0))*0.01 AS FEE FROM (
      SELECT A.HISTORY_ID, A.CAR_ID, END_DATE - START_DATE + 1 DAYS, 
          CASE 
          WHEN END_DATE - START_DATE + 1 >= 90 THEN '90일 이상'
          WHEN END_DATE - START_DATE + 1 >= 30 THEN '30일 이상'
          WHEN END_DATE - START_DATE + 1 >= 7 THEN '7일 이상'
          ELSE NULL
          END AS DURATION ,
      B.CAR_TYPE,
      B.DAILY_FEE
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
      JOIN CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID = B.CAR_ID AND B.CAR_TYPE = '트럭') C
  LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D ON C.CAR_TYPE = D.CAR_TYPE AND C.DURATION = D.DURATION_TYPE
  ORDER BY FEE DESC, C.HISTORY_ID DESC
  ```
  
  테이블 3개를 `JOIN`하여 풀이한다.

- 조회 테이블을 서브쿼리로 사용하는 복잡함을 선택하고 싶지 않았으나.. 따로 좋은 방법이 떠오르지 않는다.

- 서브쿼리 내에서 `CASE WHEN` 문을 활용하여 대여 기간 별 할인 정책 종류를 할당했다. 없다면 `NULL`값을 할당한다.

- 서브쿼리 내에서 `JOIN` 과정 중 `CAR_TYPE`이 '트럭'인 데이터만 `JOIN`하도록 했다.

- 메인쿼리에서는 할인 정책 테이블과 `LEFT OUTER JOIN`하여 할인 정책이 할당되지 않는 기록도 남도록 했다.

- 대여 일수, 일 대여 비용을 곱한 값에 할인 정책을 적용하여 산출한다.
  
  - 이때  `NVL`으로 할인 정책이 없는(대여 일수가 7일 미만인) 대여 기록은 적용이 안되도록 했다.

- 총 대여 비용과 대여 기록 ID를 내림차 순 정렬하여 출력한다.

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- 전에 어케 풀지..했던 문제인데, `CASE WHEN` 을 활용하여 할인 정책을 적용할 수 있었다.

- 대여 기록도 내림차순 정렬인데^^... 자꾸 올림차순 정렬해서 틀렸다.

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/44646
