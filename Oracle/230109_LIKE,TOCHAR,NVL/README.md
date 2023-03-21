[TOC]

# Oracle

## `LIKE`, `TO_CHAR`, `NVL`, `NVL2`

##### LIKE

- 와일드카드(%)를 사용하여 원하는 문자가 포함된 자료를 쉽게 검색할 수 있다.
  
  ```sql
  SELECT * FROM table WHERE name LIKE '박%'
  ```
  
  "박"으로 시작하는 이름을 찾는다.
  
  ```sql
  SELECT * FROM table WHERE name LiKE '%세%'
  ```
  
  "세"가 포함된 이름을 찾는다.
  
  - 앞, 뒤, 중간 어딘가에 존재한다면 해당한다.

- 언더바("_")를 사용하여 검색할 문자열의 자릿수를 결정하여 검색이 가능하다.
  
  ```sql
  SELECT * FROM table WHERE name LIKE "____" # 언더바 4
  ```
  
  문자열의 자릿수가 4인 값을 조회한다.
  
  ```sql
  SELECT * FROM table WHERE name "__세_"
  ```
  
  문자열의 자릿수가 4개이고, 3번째 자리가 "세"인 값을 조회한다.

##### TO_CHAR

- 날짜, 숫자 등의 값을 문자열로 변환하는 함수

- 날짜 포맷 변경
  
  ```sql
  SELECT TO_CHAR(SYSDATE, 'YYYYMMDD'),
         TO_CHAR(SYSDATE, 'YYYY-MM-DD')
  FROM table
  ```
  
  위와 같이 날짜 포맷(`Y`,`M`,`D`)를 사용하여 원하는 대로 출력 가능하다.

- 소수점 변경
  
  ```sql
  SELECT TO_CHAR(123.456, 'FM990.999') # 123.456
       , TO_CHAR(1234.56, 'FM9990.99') # 1234.56
  FROM table 
  ```
  
  **FM** : 문자열의 공백제거
  "9"와 "0"으로 형식을 지정한다.
  
  - "9" : 값이 없으면 표시안함, "0" : 값이 없으면 "0"으로 처리

- 숫자의 천 단위 콤마 찍기
  
  ```sql
  SELECT TO_CHAR(123456, 'FM999,999') # 123,456
       , TO_CHAR(123400567, 'FM999,999,999') # 123,400,567
  ```
  
  숫자의 최대 길이 만큼 9999...형식으로 지정한다.

- 임의의 구분자로 날짜 형식 만들기
  
  ```sql
  SELECT TO_CHAR(SYSDATE, '""YYYY"년 "MM"월 "DD"일"') # 2023년 01월 09일
       , TO_CHAR(SYSDATE, '""HH24"시 "MI"분 "SS"초"') # 15시 15분 23초
    FROM TABLE
  ```

##### NVL

- 값이 `NULL`인 경우 지정값을 출력하고, 아니라면 원래 값을 그대로 출력한다.

##### NVL2

- 값이 `NULL`이 아닌 경우 지정값1을 출력하고, `NULL`인 경우 지정값2를 출력한다.

---

- 레퍼런스

> 
