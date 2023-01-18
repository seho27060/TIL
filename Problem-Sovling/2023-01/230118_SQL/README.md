# 230118-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

- 렌트카 회사의 차량 대여 기록이 있을때, 8월에서 10월까지의 기간에서 
  
  - 차량 대여 횟수가 5회 이상인 
  
  - 자동차의 월별 
  
  - 자동차 id별 대여횟수를 출력하라. 
  
  - 월 기준으로 오름차순, 자동차id 기준 내림차순하여 출력하라.
  
  - 총 대여 횟수가 0회인 값은 제외하라.

#### 풀이과정

- 차량 대여 횟수가 5회이상을 어케 구할까나..
  
  ```sql
  SELECT CAR_ID, COUNT(CAR_ID) FROM TABLE
  WHERE COUNT(CAR_ID) >= 5
  GROUP BY CAR_ID
  ```
  
  `CAR_ID`로 그룹화한 후 해당 열을 카운트하자. 서브쿼리에 사용할 테이블이 하나 완성됐다.

- 월별, 차량별로 그룹화 후 그룹화 된 테이블에서 `COUNT(CAR_ID)`를 통해 차량의 대여 횟수를 출력한다.

- 여기서 틀리는데 자꾸 헤맨 부분이 2가지 있다.
  
  - 월을 1,2,3,4..이렇게 해야하는데 01,02,03..이렇게 나와서 그런가?
    - `TO_NUMBER()`로 01,02..형식을 1,2,3,4..이렇게 변환할 수 있다. 근데 이건 문제가 아니였다.
  - 위 서브쿼리에서 조회하는 날짜 범위를 `START_DATE`를 중심으로 2022-08부터 2022-10으로 했는데 오답이 나온다..

- 문제는 서브쿼리내에서도 8월부터 10월까지의 `START_DATE`에 해당하는 차량을 조회하고, **외부에서 `JOIN`할때도** 기간을 설정해줘야 한다.
  
  - 외부에서 기간설정을 안해서 자꾸 오답이 나왔다.

- ```sql
  SELECT
  TO_CHAR(A.START_DATE,'MM') AS MONTH, A.CAR_ID, COUNT(A.CAR_ID) AS RECORDS 
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A, (
  SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
  WHERE TO_CHAR(START_DATE,'YYYY-MM-DD') BETWEEN '2022-08-01' AND '2022-10-31'
  GROUP BY CAR_ID HAVING COUNT(CAR_ID) >= 5
  ) B 
  WHERE A.CAR_ID = B.CAR_ID AND TO_CHAR(A.START_DATE,'YYYY-MM-DD') BETWEEN '2022-08-01' AND '2022-10-31'
  GROUP BY TO_CHAR(A.START_DATE,'MM'), A.CAR_ID
  ORDER BY TO_CHAR(A.START_DATE,'MM') ASC, A.CAR_ID DESC
  ```
  
  쿼리를 보면 원본 테이블에서 파생한 테이블과 원본 테이블을 조인한다.
  
  파생된 테이블의 생성 서브쿼리내에서 기간설정을 해주고, 외부에서도 필터링해준다.
  
  - 내부에서 8월에서 10월까지의 차량 대여 횟수를 카운트하고
  
  - 외부에서도 8월에서 10월까지의 차량을 카운트해줘야
  
  - 원하는 값을 얻을 수 있다..
    
    - 외부에서 안할시 8월에서 10월까지 5회이상 대여한 차량id을 전체 기간에서 조회하게 된다.

### 카테고리 별 도서 판매량 집계하기

- 판매중인 도서 정보 테이블 `BOOK`와 판매 기록 정보 테이블 `BOOK_SALES`  이 있을때, 2022년 1월의 

- 카테고리 별 

- 도서 판매량을 합산하고 

- 카테고리, 총 판매량을 출력하라.

- 결과는 카테고리명을 기준으로 오름차순 출력

#### 풀이과정

- 2022년 1월의 도서 ID 별 총 판매량은 계산됐으나.. 도서 ID와 카테고리를 매칭해서 어떻게 카테고리로 그룹화하지?..
  
  - 파생한 테이블을 서브쿼리로 활용하려 했으나.. 도서 ID와 카테고리를 매칭하는 방법이 떠오르지 않음..

- `JOIN`도 아니고 그냥 `FROM TABLE A, TABLE B`이런식으로 출력해보다가 
  
  - 이게 `JOIN`이 어찌어찌되는거 같음 왜냐면 행이 더 많은 쪽 테이블에 공통된 컬럼으로 묶이는 듯
  
  - 그러다가 어 그럼..`BOOK` 테이블의 도서 ID와 `BOOK_SALES` 테이블의 도서 ID가 동일한 애들끼리 묶으면?...

- `WHERE BOOK.BOOK_ID = BOOK_SALES.BOOK_ID` 를 사용해서 `BOOK_ID`별로 묶었다.
  
  - 이렇게 테이블이 `BOOK_ID`로 묶이면.. `BOOK` 테이블의 `CATEGORY`도 묶이게 된다!

- 정답 코드
  
  ```sql
  SELECT BOOK.CATEGORY, SUM(BOOK_SALES.SALES) AS TOTAL_SALES FROM BOOK, BOOK_SALES
  WHERE BOOK.BOOK_ID = BOOK_SALES.BOOK_ID AND TO_CHAR(BOOK_SALES.SALES_DATE,'YYYY-MM') = '2022-01' 
  GROUP BY BOOK.CATEGORY
  ORDER BY BOOK.CATEGORY
  ```

### 성과 및 피드백

#### 성과

##### TO_NUMBER

- `DATE`와 같은 값을 `NUMBER`로 변환해준다.
  
  ```sql
  SELECT TO_CHAR(START_DATE,'MM'),TO_NUMBER(TO_CHAR(START_DATE,'MM')) FROM TABLE
  # 8과 08의 형식으로 출력된다.
  ```

##### BETWEEN \~ AND \~

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

##### WHERE 과 JOIN _ ON의 차이점

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

##### CEIL, FLOOR, TRUNC

- 올림, 내림, 버림 함수를 알아보자

- `CEIL(값)` 와 같이 사용하여 소수점의 값을 올림 할 수 있다.

- `FLOOR(값)`와 같이 사용하여 소수점의 값을 내림할 수 있다.

- `TRUNC(값, 버림할 자릿수)`로 원하는 자릿수의 값을 버림 할 수 있다.
  
  ```sql
  SELECT TRUNC(PRICE, -4) FROM BOOKS
  ```
  
  54321.0이라 할때 4번째 자릿수를 버림한다.
  
  - `ROUND`랑 비슷하다.

#### 피드백

- 조건을 잘 살펴보고

- 서브쿼리의 범위와 외부쿼리의 범위가 일치한지 고려해보자.

---

#### 레퍼런스

> [[Oracle] ROUND 함수 사용방법 (소수, 반올림, 절사)](https://gent.tistory.com/241)
