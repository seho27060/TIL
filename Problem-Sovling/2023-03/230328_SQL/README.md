# 230328-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 조건에 부합하는 중고거래 상태 조회하기

- 중고거래 게시글 테이블이 있을때,

- 2022년 10월 5일에 등록된 게시글의 

- 여러 컬럼을 출력하라. 이때 거래상태에 따라 '판매중','거래완료','예약중'을 조건 부로 출력하라

- 최종 출력은 게시글 ID를 내림차순으로 정렬하여 출력한다.

#### 풀이과정

- ```sql
  SELECT BOARD_ID, 
         WRITER_ID,
         TITLE,
         PRICE, 
         CASE 
          WHEN STATUS = 'SALE' THEN '판매중'
          WHEN STATUS = 'RESERVED' THEN '예약중' 
          WHEN STATUS = 'DONE' THEN '거래완료' END AS STATUS 
      FROM USED_GOODS_BOARD
      WHERE TO_CHAR(CREATED_DATE,'YYYY-MM-DD') = '2022-10-05'
      ORDER BY BOARD_ID DESC
  ```
  
  조건문은 어렵지 않고.. `CASE _ WHEN _ THEN` 구문을 활용하여 조건부로 출력하는게 포인트



### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 피드백

---

#### 레퍼런스

> 
