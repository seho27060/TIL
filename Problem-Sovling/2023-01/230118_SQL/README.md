# 230118-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

- 렌트카 회사의 차량 대여 기록이 있을때, 8월에서 10월까지의 기간에서 
  
  - 차량 대여 횟수가 5회 이상인 
  
  - 자동차의 월별 
  
  - 자동차 id별 대여횟수를 출력하라. 
  
  - 월 기준으로 오름차순, 자동차id 기준 내림차순하여 출력하라.
  
  - 총 대여 횟수가 0회인 값은 제외하라.

#### 풀이과정

- 차량 대여 횟수가 5회이상을 어케 구할까나..
  
  ```sql
  SELECT CAR_ID, COUNT(CAR_ID) FROM TABLE
  WHERE COUNT(CAR_ID) >= 5
  GROUP BY CAR_ID
  ```
  
  `CAR_ID`로 그룹화한 후 해당 열을 카운트하자. 서브쿼리에 사용할 테이블이 하나 완성됐다.

- 월별, 차량별로 그룹화 후 그룹화 된 테이블에서 `COUNT(CAR_ID)`를 통해 차량의 대여 횟수를 출력한다.

- 여기서 틀리는데 자꾸 헤맨 부분이 2가지 있다.
  
  - 월을 1,2,3,4..이렇게 해야하는데 01,02,03..이렇게 나와서 그런가?
    - `TO_NUMBER()`로 01,02..형식을 1,2,3,4..이렇게 변환할 수 있다. 근데 이건 문제가 아니였다.
  - 위 서브쿼리에서 조회하는 날짜 범위를 `START_DATE`를 중심으로 2022-08부터 2022-10으로 했는데 오답이 나온다..

- 문제는 서브쿼리내에서도 8월부터 10월까지의 `START_DATE`에 해당하는 차량을 조회하고, **외부에서 `JOIN`할때도** 기간을 설정해줘야 한다.
  
  - 외부에서 기간설정을 안해서 자꾸 오답이 나왔다.

- ```sql
  SELECT
  TO_CHAR(A.START_DATE,'MM') AS MONTH, A.CAR_ID, COUNT(A.CAR_ID) AS RECORDS 
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A, (
  SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  WHERE TO_CHAR(START_DATE,'YYYY-MM-DD') BETWEEN '2022-08-01' AND '2022-10-31'
  GROUP BY CAR_ID HAVING COUNT(CAR_ID) >= 5
  ) B 
  WHERE A.CAR_ID = B.CAR_ID AND TO_CHAR(A.START_DATE,'YYYY-MM-DD') BETWEEN '2022-08-01' AND '2022-10-31'
  GROUP BY TO_CHAR(A.START_DATE,'MM'), A.CAR_ID
  ORDER BY TO_CHAR(A.START_DATE,'MM') ASC, A.CAR_ID DESC
  ```
  
  쿼리를 보면 원본 테이블에서 파생한 테이블과 원본 테이블을 조인한다.
  
  파생된 테이블의 생성 서브쿼리내에서 기간설정을 해주고, 외부에서도 필터링해준다.
  
  - 내부에서 8월에서 10월까지의 차량 대여 횟수를 카운트하고
  
  - 외부에서도 8월에서 10월까지의 차량을 카운트해줘야
  
  - 원하는 값을 얻을 수 있다..
    
    - 외부에서 안할시 8월에서 10월까지 5회이상 대여한 차량id을 전체 기간에서 조회하게 된다.

### 성과 및 피드백

#### 성과

##### TO_NUMBER

- `DATE`와 같은 값을 `NUMBER`로 변환해준다.
  
  ```sql
  SELECT TO_CHAR(START_DATE,'MM'),TO_NUMBER(TO_CHAR(START_DATE,'MM')) FROM TABLE
  # 8과 08의 형식으로 출력된다.
  ```

##### BETWEEN \~ AND \~

- `DATE`, `NUMBER`형식의 값을 지정한 범위로 필터링할 수 있다.
  
  - 필터링은 `BETWEEN A AND B`일때 `A` <= 비교값 <= `B`로 비교된다.

- ```sql
  SELECT START_DATE FROM TABLE
  WHERE START_DATE BETWEEN TO_DATE('2022-08-01','YYYY-MM-DD') AND TO_DATE('2022-10-31','YYYY-MM-DD')
  ```
  
  이와 같이 문자열데이터를 `DATE`로 변환하거나
  
  ```sql
  SELECT START_DATE FROM TABLE
  WHERE TO_CHAR(A.START_DATE,'YYYY-MM-DD') BETWEEN '2022-08-01' AND '2022-10-31'
  ```
  
  `DATE`형식 데이터를 `TO_CHAR`로 문자열로 변환하여 비교가능하다.
  
  ```sql
    SELECT CAR_ID FROM TABLE
    WHERE CAR_ID BETWEEN 1234 AND 5678
  ```
  
  또는 `NUMBER`형식의 값을 위와 같이 필터링할 수 있다.

#### 피드백

- 조건을 잘 살펴보고

- 서브쿼리의 범위와 외부쿼리의 범위가 일치한지 고려해보자.

---

#### 레퍼런스

> [[Oracle] ROUND 함수 사용방법 (소수, 반올림, 절사)](https://gent.tistory.com/241)
