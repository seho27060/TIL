# 230113-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 평균 일일 대여 요금 구하기

#### 풀이과정

- "SUV" 차량의 일일 대여 요금의 평균을 소수점 첫번째 자리에서 반올림하여 출력

### 진료과별 총 예약 횟수 출력하기

#### 풀이과정

- 2022년 5월에 예약한 환자 수를 - `TO_CHAR`로 `2022-05`인 값 찾고 `COUNT(환자id)`로 환자 수 COUNT

- 진료과코드 별로 조회하라 - 진료과코드로 `GROUP BY`

- 예약 환자 수 기준으로 오름차순 정렬하고, - 예약 환자 수로 `ORDER BY ASC`

- 환자수가 같다면 진료과 코드를 기준으로 오름차순 정렬하라 - `ORDER BY`에 진료과 코드 기준 추가

### 동명 동물 수 찾기

#### 풀이과정

- 동물 이름이 두 번 이상 쓰인 이름과 - `GROUP BY(NAME)`로 그룹화 후`COUNT(NAME)`이 1을 초과하는

- 해당 이름이 쓰인 횟수를 조회 - 위 `COUNT(NAME)`으로 조회

- 이름이 없는 동물은 집계에서 제외하며 - `WHERE COUNT(NAME) > 1`로 처리

- 이름순으로 조회 - `ORDER BY NAME`으로 정렬

- ```sql
  SELECT * FROM (
    SELECT NAME, COUNT(NAME) AS "COUNT" FROM ANIMAL_INS
    GROUP BY NAME
  )
  WHERE COUNT > 1
  ORDER BY NAME
  ```
  
  위와 같이 서브쿼리를 활용하여 풀었으나.. `GROUP BY`와 `HAVING`을 사용한 답안도 있다. 아래 성과를 참고하자

### 성과 및 피드백

#### 성과

##### ROUND

- `ROUND(columns,기준 소수점 자리)`과 같은 형식으로 원하는 소수점에서 반올림한다.

- 0은 소수점 첫번째 자리, -1은 정수 첫번째 자리이다.

- ```sql
  SELECT ROUND(to_date('2019-08-12 11:50', 'yyyy-mm-dd hh24:mi')) dte_am
     , ROUND(to_date('2019-08-12 12:10', 'yyyy-mm-dd hh24:mi')) dte_pm
  FROM dual
  ```
  
  와 같이 날짜를 반올림할 수 있다.

#### GROUP BY, HAVING

- `GROUP BY`을 통해 그룹별 건수나 합계를 죄할 수 있다.

- 그룹별 집계 결과 중 원하는 조건의 결과를 필터링할땐 어떻게 해야할까?
  
  - `HAVING`을 사용하자.
    
    - `GROUP BY`를 통해 집계된 값에 대해 **집계함수**(`COUNT`, `SUM`,`AVG`,`MAX`,`MIN`)로 조건을 걸어 필터링 할 수 있다.

- ```sql
  SELECT NAME, COUNT(NAME)
  FROM ANIMAL_INS
  GROUP BY NAME
  HAVING COUNT(NAME) >= 2
  ORDER BY NAME
  ```
  
  이와 같이 `HAVING`절에 집계함수를 사용하여 조건을 걸어 필터링했다.
  이때 `GROUP BY`로 그룹화된 결과 기준으로 필터링이 걸린다.

---

#### 레퍼런스

> [[Oracle] ROUND 함수 사용방법 (소수, 반올림, 절사)](https://gent.tistory.com/241)
