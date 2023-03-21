# Oracle

## 서브쿼리 활용하기

### 다양한 서브쿼리

- `JOIN`과 분별없이 사용하던 서브 쿼리도 다양한 종류가 있다.. 사용법과 목적에 따라 아래 표와 같다.

| 서브 쿼리     | 사용 위치                 | 설명                           |
| --------- | --------------------- | ---------------------------- |
| 스칼라 서브 쿼리 | `SELECT` 절            | 단일 컬럼, 단일 로우를 반환(해당하는 1개의 값) |
| 인라인 뷰     | `FROM` 절              | View와 사용적인 측면에서 동일           |
| 중첩 서브 쿼리  | `WHERE` 절, `HAVING` 절 | 다중 컬럼 또는 다중 행을 반환            |

  또한 메인 쿼리와 연관성에 따라 연관성 없는 서브 쿼리, 연관성 있는 서브 쿼리로 분류하기도 한다.

- ```SQL
  SELECT A.ID,
           A.NAME,
         B.DEPT
         ,(SELECT C.NAME
              FROM TABLE2 C
            WHERE C.MAJOR = A.MAJOR) AS MAJOR // 스칼라 서브 쿼리
  FROM TABLE1 A,
         (SELECT X.NUMBER, // 인라인 뷰
                   X.NAME,
               Y.DEPT
        FROM TABLE1 X, TABLE3 Y
        WHERE X.MAJOR = Y.MAJOR) B
  WHERE A.LOC = B.LOC
  AND A.NUMBER IN (SELECT DISTINCT D.NUMBER // 중첩 서브 쿼리
                      FROM TABLE4 D
                    WHERE D.JOB == 'MANAGER')
  ```
  
  위 예시를 보면, `SELECT` 절, `FROM` 절, `WHERE` 절에 각각 스칼라 서브 쿼리, 인라인 뷰, 중첩 서브 쿼리를 사용한다.

#### 스칼라 서브쿼리(Scalar Subquery)

- TABLE1
  
  | ID  | NAME  | CHECK | JOB_ID |
  | --- | ----- | ----- | ------ |
  | 1   | HOSE  | 20    | 15     |
  | 2   | LINA  | 22    | 22     |
  | 3   | JAMES | 32    | 22     |
  
  TABLE2
  
  | JOB_ID | JOB | AMOUNT |
  | ------ | --- | ------ |
  | 15     | BE  | 5      |
  | 22     | FE  | 11     |
  
  위와 같은 테이블이 있을때,
  
  ```sql
  SELECT B.ID,
         B.NAME,
         (SELECT A.JOB
          FROM TABLE2 A
          WHERE A.JOB_ID = B.JOB_ID) AS JOB_NAME),
         B.CHECK - (SELECT ROUND(AVG(C.AMOUNT))
                    FROM TABLE2) AS REAL_EARN
  FROM TABLE1 B
  ```
  
  아래와 같은 결과를 출력한다.
  
  | ID  | NAME  | JOB_NAME | REAL_EARN |
  | --- | ----- | -------- | --------- |
  | 1   | HOSE  | BE       | 12        |
  | 2   | LINA  | FE       | 14        |
  | 3   | JAMES | FE       | 24        |

- `SELECT` 절에 사용하는 서브 쿼리는 **하나의 값**만 조회되어야 한다.(하나의 컬럼, 하나의 행)

- `TABLE1`의 `CHECK`에 `TABLE2`의 `AMOUNT`의 평균값을 연산할 수도 있다.

#### 인라인 뷰(Inline View)

- 평소에 `JOIN`과 같이 사용하는 서브 쿼리이다. 다른 설명을 붙이진 않겠다.
- 뷰(View)와 동일하며, 임시 뷰이기 때문에 재활용이 불가하다.
- 테이블과 달리 인덱스가 없기 때문에 데이터가 많으면 쿼리문이 느려질 수 있으므로 사용에 주의한다.

#### 중첩 서브 쿼리(Nested Subquery)

- `WHERE` 절과 같은 부분에 사용하기 때문에 여러개의 컬럼, 로우를 반환할 수 있다.
- `IN`, `EXISIT` 등등 기본에 사용하던 조건 절에 다양하게 활용 가능하다.

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/44847
> 
> [신기한 연구소 :: [HOW]SQL 서브쿼리 다양하게 사용하는 방법, 스칼라, 인라인 뷰, 중첩, 오라클(ORACLE)](https://tiboy.tistory.com/568)
> 
> [[Oracle] 오라클 서브쿼리 종류 및 사용법 (SubQuery)](https://gent.tistory.com/464)
