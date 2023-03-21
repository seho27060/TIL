# ORACLE

## TO_NUMBER, BETWEEN, JOIN-ON과 WHERE차이

### TO_NUMBER

- `DATE`와 같은 값을 `NUMBER`로 변환해준다.
  
  ```sql
  SELECT TO_CHAR(START_DATE,'MM'),TO_NUMBER(TO_CHAR(START_DATE,'MM')) FROM TABLE
  # 8과 08의 형식으로 출력된다.
  ```

### BETWEEN \~ AND \~

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

### WHERE 과 JOIN _ ON의 차이점

- [카테고리 별 도서 판매량 집계하기](###카테고리 별 도서 판매량 집계하기)에서 많은 이들이 `JOIN`으로 풀이했는데.. 나는 몰라서 `WHERE`로 풀었다. 무슨차이점이 있을까?

- **`JOIN`으로 테이블을 합치면서 필터링하느냐?**/ **`JOIN`으로 합쳐진 테이블에 다시 필터링하느냐?** 의 차이이다.
  
  - `SQL`에서는 `FROM` -> `ON` -> `JOIN` -> `WHERE` 순서로 쿼리가 실행된다.

- ```sql
  SELECT BOOK.CATEGORY, SUM(BOOK_SALES.SALES) AS TOTAL_SALES FROM BOOK, BOOK_SALES
  WHERE BOOK.BOOK_ID = BOOK_SALES.BOOK_ID AND TO_CHAR(BOOK_SALES.SALES_DATE,'YYYY-MM') = '2022-01' 
  ```
  
  위에서는 `JOIN`을 쓴건 아니지만 `FROM`에서 두개 테이블을 참고하므로.. 합쳐진 테이블 전체를 훑어 `WHERE`의 조건으로 필터링한다.

- `JOIN`으로 (가상)테이블을 생성되는 과정에서 `ON`에 할당된 조건에 의해 필터링 된 값은 채워지고 아니면 `NULL`로 남겨지게 된다.
  
  ```sql
  SELECT BOOK.CATEGORY, SUM(BOOK_SALES.SALES) AS TOTAL_SALES FROM BOOK
  JOIN BOOK_SALES
  ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
  AND TO_CHAR(BOOK_SALES.SALES_DATE,'YYYY-MM') = '2022-01'
  ```
  
  위와 같이 `WHERE`의 조건을 그대로 `ON`에 옮겨주면.. 테이블이 합쳐지면서 `ON`의 조건으로 필터링된다.

- 뭐.. 이게 좋다 나쁘다보단 각각 작동과정이 다르니 입맛에 맞게 사용해야 할듯하다.

### CEIL, FLOOR, TRUNC

- 올림, 내림, 버림 함수를 알아보자

- `CEIL(값)` 와 같이 사용하여 소수점의 값을 올림 할 수 있다.

- `FLOOR(값)`와 같이 사용하여 소수점의 값을 내림할 수 있다.

- `TRUNC(값, 버림할 자릿수)`로 원하는 자릿수의 값을 버림 할 수 있다.
  
  ```sql
  SELECT TRUNC(PRICE, -4) FROM BOOKS
  ```
  
  54321.0이라 할때 4번째 자릿수를 버림한다.
  
  - `ROUND`랑 비슷하다.

- 

---

#### 레퍼런스

> [[Oracle] ROUND 함수 사용방법 (소수, 반올림, 절사)](https://gent.tistory.com/241)
