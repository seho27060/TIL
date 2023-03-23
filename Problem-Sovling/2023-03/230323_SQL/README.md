# 230323-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기

- 중고거래 게시글, 게시글 첨부파일 테이블이 있을때,

- 조회수가 가장 높은 게시글의 첨부파일을 `FILE_ID`를 내림차순으로 하여 

- 주어진 조건대로 파일 경로를 형성하여 출력하라.

#### 풀이과정

- ```sql
  SELECT '/home/grep/src/' || CONCAT(A.BOARD_ID,'/') || A.FILE_ID || A.FILE_NAME || FILE_EXT AS FILE_PATH FROM USED_GOODS_FILE A
  JOIN (
  SELECT BOARD_ID, VIEWS FROM USED_GOODS_BOARD 
  ORDER BY VIEWS DESC
  FETCH FIRST 1 ROWS ONLY) B ON A.BOARD_ID = B.BOARD_ID
  ORDER BY A.FILE_ID DESC
  ```
  
  `CONCAT`과 `||` 로 더 명확하게 출력해봤다.

- 조회수가 가장 높은 게시글을 찾기 위해 조회수대로 내림차순 정렬하고.. `FETCH`로 첫번째 행을 조회한다.

- 해당 테이블과 첨부 파일 테이블을 `JOIN`하여 가장 높은 조회수의 게시글의 첨부파일을 찾는다.

- `||`, `CONCAT`을 활용하여 조건대로 파일 경로를 출력한다.

- `FILE_ID` 내림차순으로 출력하는건 잊지 않도록

### 성과 및 피드백

#### 성과

- 성과

#### 피드백

- 피드백

---

#### 레퍼런스

> 
