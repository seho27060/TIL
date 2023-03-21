# Oracle

## 조건에 따라 다른 값 할당하기

### CASE \~ WHEN \~ THEN \~ ELSE

### CASE \_ WHEN

- 조건을 따라 해당하는 값을 출력할 수 있는 함수이다.

- IF문 방식은 아래와 같다.
  
  ```sql
  CASE WHEN COL1 == 'EX1' THEN 'OUT1'
       WHEN COL1 == 'EX2' THEN 'OUT2'
       ELSE 'OUT3'
  END
  ```
  
  SWITCH 문 형식으로 아래와 같이 사용 가능하다.
  
  ```sql
  CASE WHEN COL1 == 'EX1' THEN 'OUT1'
     WHEN COL1 == 'EX2' THEN 'OUT2'
     ELSE 'OUT3'
  END
  ```
  
  위와 같은 식으로 사용하며, `COL1`의 값에 따라 `'OUT1'`,`'OUT2'`가 출력되며 해당 하지 않는다면 `'OUT3'`가 출력된다.

- `ELSE`부분은 생략 가능하다.

- `ELSE`가 생략된 상태에서 어느 조건에도 만족하지 못한다면 `NULL`이 출력된다.

---

#### 레퍼런스

> 
