# 230320-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 조건에 맞는 사용자 정보 조회하기

- 중고거래 게시글, 중고거래 사이트 유저 테이블이 있을때,

- 거래 게시글을 3회 이상 게시한 유저의 정보를 출력하라.

- 유저 ID를 내림차순으로 출력

#### 풀이과정

- ```sql
  SELECT USER_ID, NICKNAME, CITY || ' ' || STREET_ADDRESS1 || ' ' || STREET_ADDRESS2, SUBSTR(TLNO,0,3) || '-' || SUBSTR(TLNO,4,4) || '-' || SUBSTR(TLNO,8,4) FROM USED_GOODS_USER
  WHERE USER_ID IN (SELECT WRITER_ID FROM USED_GOODS_BOARD
  GROUP BY WRITER_ID HAVING COUNT(WRITER_ID) >= 3)
  ORDER BY USER_ID DESC
  ```
  
  `CONCAT`을 사용했다가, `||` 로 더 쉽게 출력했다.

- 중고 거래 게시글 테이블 `USED_GOODS_BOARD`에서 `WRITER_ID`로 그룹화하면서 `HAVING`절에 `WRITER_ID`가 3개 이상인 경우로 서브쿼리를 만든다.

- 3개의 다른 컬럼의 문자열을 공백으로 붙여 출력하거나..

- 1개 컬럼의 긴 문자열에 구분자를 삽입하여 출력하거나..하는 조건이 달른 출력을 원한다.

- `CONCAT`으로 문자열을 붙이는 건 알겠는데.. `TLNO`에 구분자를 삽입하는건?...
  
  - `CONCAT`과 동일한 작업을 수행하는 `||`연산자로 풀이했다.
  
  - 같은 기능을 하지만, 훨씬 더 가독성이 좋다.

- `USER_ID`가 3회 이상 작성한 `WRITER_ID` 서브쿼리에 있는지 확인 후 `USER_ID`로 내림차순 정렬하여 출력

### 성과 및 피드백

#### 성과

##### CONCAT, \||

- 문자열을 붙이는 함수로 `CONCAT`이 있다.
  
  | TABLE1 | JOB | NAME |
  | ------ | --- | ---- |
  |        | 개발자 | 박세호  |
  
  위와 같은 테이블이 있다고 할때, `JOB`과 `NAME`을 붙여서 출력해보자.
  
  ```sql
  SELECT CONCAT(JOB,NAME),CONCAT(JOB,CONCAT('-',NAME)) FROM TABLE1
  ```
  
  아래와 같이 출력한다.
  
  | RESULT | CONCAT(JOB,NAME) | CONCAT(JOB,CONCAT('-',NAME)) |
  | ------ | ---------------- | ---------------------------- |
  |        | 개발자박세호           | 개발자-박세호                      |
  
  `CONCAT`을 연쇄적으로 이어붙여야한다.. 가독성이 떨어지고 구찮다.

- 그런 당신을 위한 `||`연산자, `CONCAT`과 같은 기능을 하면서 훨씬 간단하게 작성할 수 있다.
  
  ```sql
  SELECT JOB || NAME, JOB||'-'||NAME FROM TABLE1
  ```
  
  `CONCAT`을 중복하여 연쇄적으로 안써도 되고, 연산하는 `||` 자체 만으로 구분되어 출력이 쉽게 예상된다.
  
  결과는 `CONCAT`의 예시와 동일하다!

#### 피드백

- 피드백

---

#### 레퍼런스

> 
