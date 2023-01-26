# 230126-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 자동차 대여 기록에서 장기/단기 대여 구분하기

- 대여 기간에 따라 "장기 대여" 혹은 "단기 대여"라는 새로운 컬럼을 붙여 출력하라.

#### 풀이과정

- 오우 쉣 무슨 새로운 컬럼을 붙여서 출력하래.

- `CASE WHEN _ THEN _ END` 구문으로 해결했다.

- `LEVEL 1`이지만 그렇지 못한 난도

### 중성하 여부 파악하기

- 동물 보호소에 들어온 기록인 `ANIMAL_INS`와 입양나간 기록에서 `SEX_UPOM_INTAKE`컬럼을 확인하여 중성화 여부를 출력하라

#### 풀이과정

- `CASE WHEN _ THEN _ END` 문으로 해결했다.
  
  ```sql
  SELECT ANIMAL_ID, NAME, 
  CASE 
    WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O' 
    ELSE 'X' 
    END AS 중성화
  FROM ANIMAL_INS
  ORDER BY ANIMAL_ID
  ```
  `CASE`문 안에서 `OR`를 활용하여 두개 조건을 할당했다.

### 성과 및 피드백

#### 성과

##### CASE \_ WHEN

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

#### 피드백

- 데이터 테이블가 어떤 상태인지 잘 확인하자
- 서브쿼리 형성 후 `JOIN`, `JOIN`과정에서 그룹화 및 집계량 추출.. 어떤 방법이 더 효율적일까에 대한 고민

---

#### 레퍼런스

> [[ORACLE] 행 제한 — IT 일기](https://jjoyling.tistory.com/38)
