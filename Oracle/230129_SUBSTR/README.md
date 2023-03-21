# Oracle

## 문자열의 부분 다루기

### SUBSTR

- 문자열을 자를때 사용하는 함수이다.

- `SUBSTR(컬럼, 시작위치, 길이)` 로 사용한다.

- ```sql
  # ABCDEF, XYZ123 이라는 데이터가 있다고 할때
  SELECT SUBSTR(COLUMN,1, 3), SUBSTR(COLUMN,4,6) FROM TABLE
  # [ABC,XYZ], [DEF,123]이 각각 출력된다.
  ```

---

#### 레퍼런스

> [[ORACLE] 행 제한 — IT 일기](https://jjoyling.tistory.com/38)
