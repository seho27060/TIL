# 230215-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 취소되지 않은 진료 예약 조회하기

- 환자 테이블, 의사 테이블, 예약 테이블이 있을때,

- `2022-04-13`의 예약이 취소되지 않으며 진료과목이 `CS`인 예약 내역을 조회하라

- 진료예약일시를 오름차순으로 정렬하여 출력

#### 풀이과정

- ```sql
  SELECT A.APNT_NO, C.PT_NAME,A.PT_NO,A.MCDP_CD,B.DR_NAME,A.APNT_YMD FROM APPOINTMENT A
  JOIN DOCTOR B ON A.MDDR_ID = B.DR_ID AND (TO_CHAR(A.APNT_YMD,'YYYY-MM-DD') = '2022-04-13' AND A.MCDP_CD = 'CS' AND (A.APNT_CNCL_YN = 'N' OR A.APNT_CNCL_YN IS NULL))
  JOIN PATIENT C ON A.PT_NO = C.PT_NO
  ORDER BY A.APNT_YMD
  ```
  
  테이블 3개를 조인하여 사용한다.

- 조건에 필요한 값들이 `APPOINTMENT` 테이블에 모두 있다.

- `DOCTOR`, `PATIENT` 테이블과 조인할때, 조건을 넣어준다.

- `JOIN` 기준은 각각의 키 관계에 맞도록 할당

- 마지막에 `A.APNT_YMD`를 기준으로 출력

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- 

---

#### 레퍼런스

> 
