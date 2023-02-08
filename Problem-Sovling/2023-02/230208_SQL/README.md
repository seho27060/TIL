# 230208-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 입양 시각 구하기(2)

- 입양 보낸 동물 리스트가 있을때, 입양 시간대별로 입양 건이 몇건인지 출력하라.
- 시간대 순으로 정렬하여 출력한다.

#### 풀이과정

- `GROUP BY`로 `TO_CHAR(DATETIME,'hh24')`를 기준으로 그룹화하고, `COUNT(DISTINCT ANIMAL_ID)`로 입양 건을 센다.

- 근데 안된다 왜냐, 00시에 입양 횟수가 0이면 데이터가 없어서 그룹화가 안된다..
  
  - 결국 입양이 없는 시간은 출력도 안된다.
  
  - 문제에서는 입양이 없다면 0으로 표현하길 원한다.

- 가상의 테이블을 붙여 0의 값을 출력해야하는데.. 답은 `LEVEL - CONNECT ~`로 0에서 23까지의 값을 갖는 컬럼을 만든 후에, `UNION`이나 `JOIN`으로 테이블을 합친다.

- ```sql
  SELECT HOUR, SUM(COUNT) AS COUNT FROM(
    SELECT TO_NUMBER(TO_CHAR(DATETIME, 'hh24')) AS HOUR
          ,COUNT(DISTINCT ANIMAL_ID) AS COUNT 
    FROM ANIMAL_OUTS
    GROUP BY TO_NUMBER(TO_CHAR(DATETIME, 'hh24'))
  
    UNION
  
    SELECT LEVEL-1 AS HOUR, 0 as COUNT 
    FROM DUAL
    CONNECT BY LEVEL < 25
  )
  GROUP BY HOUR
  ORDER BY HOUR
  ```
  
  `SELECT`를 3번이나 사용하여 비효율적으로 보이나..흠.. 좋은 방법이 더없나.

### 성과 및 피드백

#### 성과

##### DUAL

- 오라클 데이터베이스 설치본에 기존으로 존재하는 1개 열로 구성된 임시 테이블
  
  - 소유자는 `SYS`로 누구나 사용가능하며
  
  - 스키마가 없어 자유롭게 사용할 수 있다.

- ```sql
  SELECT SYSDATE FROM DUAL
  SELECT 'TEST' FROM DUAL
  ```
  
  위와 같이 사용 가능하며, 내장함수(`SYSDATE`...), 사용자 함수, 특정 값을 보여주고자 할 때 사용가능하다.

##### CONNECT BY ~ LEVEL

- `ORACLE`에서 사용하는 `CONNECT BY`를 활용한 계층적 쿼리
- `LEVEL`은 `ORACLE`에서 실행되는 모든 쿼리 내에서 사용 가능한 **"가상의 열"** 이다.
- ```sql
  SELECT LEVEL AS RANK
  FROM DUAL
  CONNECT BY LEVEL < 25
  ```
  
  위와 같은 쿼리는 가상 테이블 `DUAL`을 활용하여 가상 컬럼 `LEVEL`을 출력한다.
  이때 `CONNECT BY`에 조건을 할당한다.
  - `계층적 쿼리`와 관련 된 내용이지만, 차후에 기록하겠다.

#### 피드백

- 모르는게 투성

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/42752
> 
> https://school.programmers.co.kr/questions/42153
> https://velog.io/@sjwngjs/Oracle-Dual-%EC%9D%B4%EB%9E%80
> 
> https://velog.io/@seulgi/CONNECT-BY-LEVEL-%ED%99%9C%EC%9A%A9
