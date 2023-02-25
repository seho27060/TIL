# 230225-PGMS-SQL

## SQL 고득점 kit - ORACLE

### 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기

- 차 대여 기록에서 `2022-11`에 1달 동안 대여가 가능하고

- 차 종류가 "세단"이나 "SUV"인 차량중

- 할인 정책을 적용했을때 비용이 50만원 이상 200만원 미만인 차량의

- `CAR_ID`, `CAR_TYPE`, `FEE`를 출력하라.

#### 풀이과정

- ```sql
  SELECT A.CAR_ID, A.CAR_TYPE,A.DAILY_FEE*30*(1-0.01*B.DISCOUNT_RATE) AS FEE FROM CAR_RENTAL_COMPANY_CAR A
  JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN B ON A.CAR_TYPE = B.CAR_TYPE AND B.DURATION_TYPE ='30일 이상' AND
      (A.CAR_TYPE = 'SUV' OR A.CAR_TYPE = '세단')
  WHERE A.CAR_ID NOT IN (
      SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE ('2022-11-01' BETWEEN TO_CHAR(START_DATE,'YYYY-MM-DD') AND TO_CHAR(END_DATE,'YYYY-MM-DD') OR
             '2022-11-30' BETWEEN TO_CHAR(START_DATE,'YYYY-MM-DD') AND TO_CHAR(END_DATE,'YYYY-MM-DD'))
      GROUP BY CAR_ID) AND
      A.DAILY_FEE*30*(1-0.01*B.DISCOUNT_RATE) BETWEEN 500000 AND 1999999
  ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC
  ```
  
  테이블 3개를 `JOIN`하여 풀이한다. 대단히 복잡하다.

- 우선 11월 한달동안 대여기록이 있는 차량을 제외하기 위해 해당 기간에 대여 기록이 있는 차량을 `CAR_RENTAL_COMPANY_RENTAL_HISTORY`에서 추려낸다.
  
  - 해당 기록은 서브쿼리로 사용하여 메인 쿼리의 `WHERE`에 조건 할당에 사용한다.
    
    ```sql
        SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE ('2022-11-01' BETWEEN TO_CHAR(START_DATE,'YYYY-MM-DD') AND TO_CHAR(END_DATE,'YYYY-MM-DD') OR
           '2022-11-30' BETWEEN TO_CHAR(START_DATE,'YYYY-MM-DD') AND TO_CHAR(END_DATE,'YYYY-MM-DD'))
    GROUP BY 
    ```

- `JOIN`을 실행하면서 문제에서 원하는 조건을 할당하고

- 동시에 할인 정책 `CAR_RENTAL_COMPANY_DISCOUNT_PLAN`을 참고하여 "30일 이상" 정책의 할인율을 적용한 30일 간의 대여 비용을 조건에 활용하고 출력한다.

- 문제에서 원하는 대로 정렬하여 출력

### 성과 및 피드백

#### 성과

##### 

#### 피드백

- 테이블 3개를 `JOIN`하는 것도 모잘라 여러 히스토리 기록에서 특정기간에 속한지 확인하고...

- 쉽지 않다. 특히 날짜 범위에 해당되는지 안되는지 판단하는 `WHERE`의 조건을 구성할때 진땀좀 뺐다;;

---

#### 레퍼런스

> https://school.programmers.co.kr/questions/44220
