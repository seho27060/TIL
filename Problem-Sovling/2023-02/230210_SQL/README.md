# 230210-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 그룹별 조건에 맞는 식당 목록 출력하기

- 리뷰를 남긴 유저 데이터 `MEMBER_PROFILE`과 식당 리뷰 리스트 데이터 `REST_REVIEW`를 활용하여

- 리뷰를 가장 많이 남긴 사람들이

- 남긴 리뷰를 출력하라

- 리뷰 작성일, 리뷰 텍스트 기준으로 오름차순 출력하라.

#### 풀이과정

- ```sql
  SELECT C.MEMBER_NAME, A.REVIEW_TEXT, TO_CHAR(A.REVIEW_DATE,'YYYY-MM-DD') AS REVIEW_DATE FROM REST_REVIEW A
  JOIN (SELECT MEMBER_ID
        ,COUNT(REVIEW_ID) AS REVIEW_COUNT 
        ,RANK() OVER (ORDER BY COUNT(REVIEW_ID) DESC ) AS RANK
        FROM REST_REVIEW 
        GROUP BY MEMBER_ID) B ON A.MEMBER_ID = B.MEMBER_ID
  JOIN MEMBER_PROFILE C ON A.MEMBER_ID = C.MEMBER_ID
  WHERE B.RANK = 1
  ORDER BY REVIEW_DATE, REVIEW_TEXT
  ```
  
  아휴.. 복잡해. 3개의 테이블을 `JOIN`했다.

- 서브쿼리 내의 데이터는 `REST_REVIEW` 데이터를 멤버별로 그룹화하여 리뷰 개수(`COUNT(REVIEW_ID)`)를 구하고 그와 동시에 `RANK() OVER`를 통해 리뷰 개수에 따른 순위를 할당하여 출력했다.

- 이휴 리뷰 데이터 `REST_REVIEW`와 리뷰 개수별 랭크를 할당한 리뷰 멤버 리스트 서브쿼리와 리뷰 유저 데이터 `MEMBER_PROFILE`을 `MEMBER_ID`를 기준으로 묶어줬다.

- 이후 문제에서 원하는 `MEMBER_NAME` , `REVIEW_TEXT`, `REVIEW_DATE`를 형식대로 출력한다.

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- `RANK` 숙지를 못해서 또 찾아봤다.

- 복잡한 쿼리라면 사용자함수를 구현하여 사용하자.

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/42123
