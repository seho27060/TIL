# Oracle

## 출력시에 원하는 개수의 행 출력하기

### OFFSET

### OFFSET \~

#### 행 제한

- 원하는 조건에 따라 행 개수를 제한한다

- 기본 사용 구조는 아래와 같다.
  
  ```sql
  OFFSET 건수 { ROW | ROWS }
  FETCH {FIRST | NEXT} {건수 | 숫자 PERCENT}
  {ROW | ROWS}
  {ONLY | WITH TIES}
  ```

- `OFFSET`을 통해 조회하는 행의 시작 지점(건수)를 지정하고

- `FETCH`로 반환할 행 또는 비율(`PERCENT`)를 지정한다.

- `ONLY`로 지정한 정확한 값만 반환한다.

- `FETCH`와 `NEXT`, `ROW`와 `ROWS`의 기능의 차이는 없다.

- 행 개수의 3%만 반환할때는 
  
  ```sql
  SELECT NAME, ID FROM TABLE
  ORDER BY ID
  FETCH FIRST 3 PERCENT ROWS ONLY;
  ```

- 행 개수를 3부터 3개만 반환한다면
  
  ```sql
  SELECT NAME, ID FROM TABLE
  ORDER BY ID
  OFFSET 3 ROWS FETCH FIRST 3 PERCENT ROWS ONLY;
  ```
  
  이러면 `ROWNUM`이 3, 4, 5인 값이 반환된다.

#### 피드백

- 데이터 테이블가 어떤 상태인지 잘 확인하자
- 서브쿼리 형성 후 `JOIN`, `JOIN`과정에서 그룹화 및 집계량 추출.. 어떤 방법이 더 효율적일까에 대한 고민

---

#### 레퍼런스

> [[ORACLE] 행 제한 — IT 일기](https://jjoyling.tistory.com/38)
