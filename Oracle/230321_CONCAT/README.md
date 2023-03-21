# Oracle

## 문자열 이어붙이기

### CONCAT, \||

#### CONCAT

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

#### ||

- 그런 당신을 위한 `||`연산자, `CONCAT`과 같은 기능을 하면서 훨씬 간단하게 작성할 수 있다.
  
  ```sql
  SELECT JOB || NAME, JOB||'-'||NAME FROM TABLE1
  ```
  
  `CONCAT`을 중복하여 연쇄적으로 안써도 되고, 연산하는 `||` 자체 만으로 구분되어 출력이 쉽게 예상된다.
  
  결과는 `CONCAT`의 예시와 동일하다!

---

#### 레퍼런스

> [[Oracle] 오라클 문자열 합치는 방법 (||, CONCAT)](https://gent.tistory.com/256)
