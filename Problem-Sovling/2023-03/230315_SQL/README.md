# 230315-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 조건에 부합하는 중고거래 댓글 조회하기

- 중고거래 게시글, 중고거래 게시글 댓글 테이블이 있을때,

- 2022년 10월에 작성된 "게시글 또는 댓글"을 출력하라.

- 댓글의 생성날짜, 게시글 제목 순으로 정렬하여 출력한다.

#### 풀이과정

- ```sql
  SELECT B.TITLE, B.BOARD_ID, A.REPLY_ID, A.WRITER_ID, A.CONTENTS, TO_CHAR(A.CREATED_DATE,'YYYY-MM-DD') AS CREATED_DATE FROM USED_GOODS_REPLY A
  JOIN USED_GOODS_BOARD B ON A.BOARD_ID = B.BOARD_ID
  WHERE TO_CHAR(A.CREATED_DATE,'YYYY-MM') = '2022-10' OR TO_CHAR(B.CREATED_DATE,'YYYY-MM') = '2022-10'
  ORDER BY A.CREATED_DATE, B.TITLE
  ```
  
  `SELECT`로 분류된 문제인데 쉽지않다;;

- 문제 지문이 조금 헷갈린다, 댓글을 출력하는데 생성 날짜가 게시글 기준인지, 댓글 기준인지.

- 댓글과 게시글 테이블을 `JOIN`하여 댓글의 생성 날짜 또는 게시글의 생성 날짜가 2022년 10월인 **"댓글"** 을 출력해야 한다.
  
  - 댓글만 날짜에 해당하는게 아닌, 게시글의 생성 날짜가 해당되는 댓글도 포함이다.

- 그리고 조건에 맞춰 정렬하여 출력한다.

### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 피드백

---

#### 레퍼런스

> 
