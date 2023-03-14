# 230314-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 조건에 맞는 사용자 정보 조회하기

- 고객 정보, 고객의 중고 거래 두개 테이블을 사용하여

- 각 고객 마다 완료된 중고거래의 거래액의 총합이 

- 70만원 이상인 사용자 정보를 출력하라.

#### 풀이과정

- ```sql
  SELECT A.USER_ID, A.NICKNAME, B.TOTAL_SALES FROM USED_GOODS_USER A 
  LEFT JOIN (SELECT WRITER_ID, SUM(PRICE) AS TOTAL_SALES FROM USED_GOODS_BOARD
  WHERE STATUS LIKE 'DONE'
  GROUP BY WRITER_ID) B
  ON A.USER_ID = B.WRITER_ID
  WHERE B.TOTAL_SALES >= 700000
  ORDER BY B.TOTAL_SALES
  ```
  
  `GROUP BY`로 사용자 이름별로 그룹화된 데이터에서 `SUM`으로 거래액 합을 구했다.

- 조건으로 거래 상태 `STATUS`가 `'DONE'`인 조건도 걸어주고

- 해당 결과와 사용자 데이터를 `USER_ID`와 `WRITER_ID`를 매칭하여 `JOIN`한다.

- 결과는 총액을 오름차순 정렬하여 출력

### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 피드백

---

#### 레퍼런스

> 
