# 230209-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 자동차 대여 기록에서 대여중/ 대여 가능 여부 구분하기

- 자동차 대여 기록에서 `2022-10-16`의 날짜에 대여 가능한 차량은 "대여 가능"

- 아니라면 "대여중" 이라고 출력하라.

- 이때 `CAR_ID`를 기준으로 내림차순 정렬하여 `CAR_ID`별로 출력하라.

#### 풀이과정

- 특정날짜(`2022-10-16`)에 대여가 가능한지 확인하기 위해 일자의 범위 기준을 잘 잡아야 한다..
  
  - 이게 좀 헷갈렸다. `START_DATE` 를 작아야하는 작거나 같아야하는지..
  
  - 결론은 `START_DATE`는 특정날짜보다 작거나 같고(`AND`) `END_DATE`는 특정 날짜보다 크거나 같다면 "대여중"인 차량이다.

- 데이터가 여러대의 차량의 대여 기록이고, 대여 기록이 잘 기록되었다면 겹치는 시간 없이 대여가 진행됐다.

- 따라서 구한다면 1개 차량별로 대여 여부가 조회된다.

- 위에서 구한 테이블과 `CAR_ID`의 리스트를 컬럼으로 갖는 테이블과 `UNION`하여 새로운 테이블을 만들고

- 다시 해당 테이블에 `GROUP BY`와 `NVL`로 대여 가능 여부를 출력했다.

- ```sql
  SELECT CAR_ID, CASE WHEN SUM(AVAILABILITY) IS NULL THEN '대여 가능' ELSE '대여중' END AS AVAILABILITY FROM 
  (SELECT DISTINCT CAR_ID, NULL AS AVAILABILITY FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
   UNION
   SELECT CAR_ID, 1 AS AVAILABILITY FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
   WHERE '2022-10-16' BETWEEN TO_CHAR(START_DATE,'YYYY-MM-DD') AND TO_CHAR(END_DATE,'YYYY-MM-DD')
  )
  GROUP BY CAR_ID
  ORDER BY CAR_ID DESC
  ```
  `UNION`으로 중복되는 차량이 기록된 테이블을 `GROUP BY`로 그룹화하여 `SUM(AVAILABILITY)`의 값을 `CASE WHEN`구문으로 대여 여부를 출력했다 ㅎ..
  왤케 복잡하게 한건지 허허

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- "대여 가능"을 "대여가능" 이라고 해서 자꾸 오답이 나왔다 ㅠ.. 기초적인 실수라니

- `UNION`, `CASE WHEN THEN ELSE END`, `BETWEEN`, `NVL` 등등 분명 기록했는데 자꾸 까먹는다 ^^...

---

#### 레퍼런스

> 
