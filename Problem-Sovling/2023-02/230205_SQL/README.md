# 230205-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 저자 별 카테고리 별 매출액 집계하기

- 도서 정보 테이블 `BOOK`, 저자 정보 `AUTHOR`, 책 판매 테이블 `BOOK_SALES` 등 3개(!!)의 데이터가 있을때
- 2022년 1월에 판매된 책들의 
- 저자 별
- 카테고리 별
- 매출액을 구하여
- `AUTHOR_ID`, `AUTHOR_NAME`, `CATEGORY`, `SALES`를 출력하라
- 결과는 `AUTHOR_ID`를 오름차순, `CATEGORY`를 내림차순으로 정렬한다.

#### 풀이과정

- 3개 테이블을 활용해서 출력해야 한다!..

- 나는 `JOIN`을 2번 사용했다. 서브쿼리 내에서 1번, 메인 쿼리에서 1번..
  
  - 다른 사람 정답보니 한번의 `JOIN`에서 `ON`에 여러 기준 컬럼을 줄수도 있따. 나중에 설명하겠다.

- 서브쿼리에서는 `BOOK`과 `AUTHOR`를 `JOIN`했다.
  
  ```sql
  SELECT A.BOOK_ID,A.CATEGORY,A.AUTHOR_ID,A.PRICE,B.AUTHOR_NAME FROM BOOK A
      JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
  ```
  
  DF

- 위 서브쿼리와 `BOOK_SALES`로 생성한 서브쿼리를 `JOIN`한다. 
  
  ```sql
  SELECT BOOK_ID,SUM(SALES) AS SUM_SALES FROM BOOK_SALES
          WHERE TO_CHAR(SALES_DATE, 'YYYY-MM') = '2022-01'
          GROUP BY BOOK_ID
  ```
  
  2022년 1월에 해당하는 데이터를 `BOOK_ID`로 그룹화했다.

- 이후,, `AUTHOR_ID`,`AUTHOR_NAME`, `CATEGORY`로 그룹화하여 `PRICE`와 서브쿼리에서 구한 매출량 `SUM_SALES`를 `SUM`한 집계값을 출력한다.
  
  ```sql
  SELECT C.AUTHOR_ID,C.AUTHOR_NAME,C.CATEGORY,SUM(C.PRICE*D.SUM_SALES) AS TOTAL_SALES FROM (
      SELECT A.BOOK_ID,A.CATEGORY,A.AUTHOR_ID,A.PRICE,B.AUTHOR_NAME FROM BOOK A
      JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID) C
      JOIN (SELECT BOOK_ID,SUM(SALES) AS SUM_SALES FROM BOOK_SALES
            WHERE TO_CHAR(SALES_DATE, 'YYYY-MM') = '2022-01'
            GROUP BY BOOK_ID
           ) D ON C.BOOK_ID = D.BOOK_ID
  GROUP BY C.AUTHOR_ID,C.AUTHOR_NAME,C.CATEGORY
  ORDER BY C.AUTHOR_ID ASC, C.CATEGORY DESC
  ```

### 성과 및 피드백

#### 성과

#### 피드백

- `GROUP BY`로 컬럼 별로 그룹화를 할때는, 관련 컬럼이나 집계함수만 출력이 가능하다.
  
  - `NAME`이 "SEHO"인 행이 2개이고 `AMOUNT`의 값이 2,100으로 두개의 값일때, `NAME`으로 `GROUP BY`하면서 `AMOUNT`의 값을 출력하면 안나온다..
  - 이때 예시가 `INTEGER`인데, `DATE`, `BOOLEAN`다 똑같이 적용된다.

- `ORACLE`에서 `JOIN`으로 새로운 테이블을 생성하면 결합 기준이 되거나 중복되는 이름을 갖는 컬럼은 그대로 중복으로 생성된다.
  
  - 이때 생성된 테이블을 다시 `JOIN`할때, 중복되는 컬럼의 이름이 이상하게 출력되므로, 적절한 처리를 해주자(EX: 중복되는 컬럼중 1개만 조회되도록 설정)

- 오늘 풀이한 "저자 별 카테고리 별 매출액 집계하기"의 답안은 아래와 같이 풀이할 수도 있다.
  
  ```sql
  SELECT B.AUTHOR_ID,A.AUTHOR_NAME,B.CATEGORY,SUM(S.SALES*B.PRICE) AS TOTAL_SALES
  FROM BOOK_SALES S, BOOK B, AUTHOR A
  WHERE S.BOOK_ID = B.BOOK_ID
  AND B.AUTHOR_ID = A.AUTHOR_ID
  AND   TO_CHAR(S.SALES_DATE,'YYYYMM')='202201'
  GROUP BY  B.AUTHOR_ID,A.AUTHOR_NAME,B.CATEGORY
  ORDER BY 1 , 3 DESC;
  ```
  
  3개 테이블을 `JOIN`하면서.. `WHERE`문에 기준이 되는 컬럼을 여러개 할당했다.
  왜 `JOIN` 기준을 여러개 할 걸 생각 못했을까 ㅎ..

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/42834
