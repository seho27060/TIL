# Oracle

## `NULL` 조건 걸기, `JOIN`의 종류

### IS NULL, JOIN의 종류

#### IS NULL

- 특정 컬럼의 행 값이 `NULL`인 조건을 추가할 수 있다.
  
  ```sql
  SELECT ANIMAL_ID FROM ANIMAL_INS
  WHERE NAME IS NULL
  ORDER BY ANIMAL_ID
  ```

- `IS NOT NULL`을 하면 `NULL`이 아닌 값을 찾을 수 있다.

#### JOIN

- 테이블간의 공통된 컬럼으로 데이터를 합쳐 표현하는 것.

- `INNER JOIN`과 `OUTER JOIN`이 있다.

- `TABLE1` 이라는 테이블은 아래와 같고,
  
  | NAME  | ID  |
  | ----- | --- |
  | JAMES | 11  |
  | TOMMY | 22  |
  | SHERY | 33  |
  
  `TABLE2` 이라는 테이블은 아래와 같다고 하자.
  
  | ID  | TYPE  |
  | --- | ----- |
  | 15  | MAN   |
  | 22  | MAN   |
  | 33  | WOMAN |
  | 44  | WOMAN |

- `INNER JOIN`
  
  - ```sql
    SELECT A.NAME
        , A.ID
        , B.TYPE
    FROM TABLE1 A
    INNER JOIN TABLE2 B
        ON A.ID = B.ID
    ```
    
    위와 와 같이 사용한다.
  
  - 내부 조인(`INNER JOIN`)에서는 메인 테이블(`TABLE1`)과 조인 테이블(`TABLE2`)에 조인 컬럼(`ID`)의 값이 **동시에 존재해야 조회**가 된다.
  
  - 결과는 아래와 같다. 두개 테이블에 동시에 존재하는 데이터를 두개 테이블을 합쳐서 조회한다.
    
    | NAME  | ID  | TYPE  |
    | ----- | --- | ----- |
    | TOMMY | 22  | MAN   |
    | SHERY | 33  | WOMAN |

- `LEFT OUTER JOIN`
  
  - ```sql
    SELECT A.NAME
        , A.ID
        , B.TYPE
    FROM TABLE1 A
    LEFT OUTER JOIN TABLE2 B
        ON A.ID = B.ID
    ```
    
    `TABLE1`과 `TABLE2`를 외부 조인(`OUTER JOIN`)하여 `TABLE2.TYPE`을 조회했다.
  
  - `OUTER JOIN`에서는 조인 테이블(`TABLE2`)의 값이 **존재하지 않아도** 메인 테이블(`TABLE1`)의 값이 조회된다.
  
  - 이때 가져오지 못하는 값은 `NULL`로 표현된다.'
  
  - 결과는 아래와 같다. `TABLE2` 에 없는 `JAMES`의 값은 조회되지 않아 `NULL`로 표현되었다. 
    
    | NAME  | ID  | TYPE  |
    | ----- | --- | ----- |
    | JAMES | 11  | NULL  |
    | TOMMY | 22  | MAN   |
    | SHERY | 33  | WOMAN |
    
    `LEFT OUTER JOIN`이므로 메인 테이블(`TABLE1`)은 왼쪽에 위치하게 된다.

- `RIGHT OUTER JOIN`
  
  - `LEFT OUTER JOIN`과 비슷하다. 다른 점은 조인될때 메인 테이블이 오른쪽에 위치하게 된다.
  
  - `OUTER JOIN`의 **핵심**은 **메인 테이블의 데이터는 무조건 조회**되고, **조인 테이블은 참조** 용도로 사용된다.

- `CROSS JOIN`
  
  - 두 테이블의 모든 데이터를 서로 한 번씩 조인을 한다.
  
  - ```sql
    SELECT TABLE1.NAME
        , TABLE2.ID
        , TABLE2.TYPE
    FROM TABLE1
    CROSS JOIN TABLE2
    WHERE TABLE2.ID IN (15,22,33,44)
    ```
    
    위와 같이 조인할 시, `TABLE1`의 3개 행과 `TABLE2`의 4개 행이 서로 조인되어 12개 행을 갖는 테이블이 조회된다.
  
  - 조인보다는.. 그냥 갖다 붙이는거긴 하다.

---

#### 레퍼런스

> [[Oracle] 오라클 조인 방법 쉽게 설명 (ANSI JOIN, Oracle Join)](https://gent.tistory.com/469)
