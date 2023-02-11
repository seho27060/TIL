# Nomalization

## 정규화

> 관계형 데이터베이스의 설계에서 중복을 최소화하게 데이터를 구조화하는 프로세스

- 기본 목표는 테이블 간의 중복된 데이터를 허용하지 않는 것.
  
  - 중복된 데이터를 허용하지 않음으로써 **무결성(Integrity)** 을 유지할 수 있으며, DB의 저장 용량 역시 줄일 수 있다.

### 정규화의 단계

- 정규화를 위해 테이블을 분해하는 정규화 단계는 아래와 같이 분류되어 있다.

#### 제1 정규화

> 테이블의 컬럼이 원자값(Atomic Value, 하나의 값)을 갖도록 테이블을 분해하는 것

- 즉 각 컬럼의 레코드는 하나의 값만 갖도록 한다. 

- | TABLE1 | NAME | LANGUAGE               |
  | ------ | ---- | ---------------------- |
  |        | HOSE | KOREAN,ENGLISH         |
  |        | LINA | KOREAN.ENGLISH.RUSSIAN |
  
  위 테이블에서 `HOSE`와 `LINA`는 각각 2개국어, 3개 국어를 할 수 있음을 확인할 수 있다. 이러한 레코드는 하나의 컬럼의 레코드에 여러개의 의미를 갖는다.

- 위 데이터에 "제1 정규화"로 테이블을 분해한다면 아래와 같다.
  
  | TABLE2 | NAME  | LANGUAGE |
  | ------ | ----- | -------- |
  |        | HOSE  | ENGLISH  |
  |        | LINA  | ENGLISH  |
  |        | HOSE  | KOREAN   |
  |        | LINA  | KOREAN   |
  |        | LINAK | RUSSIAN  |
  
  컬럼의 하나의 레코드는 "한 개"의 언어를 의미하는 원자값이 되었다. 

- 이러한 데이터를 **제1 정규형** 테이블이라고 한다.

#### 제2 정규화

> 제1 정규형 테이블을 **완전 함수 종속**을 만족하도록 테이블을 분해하는 것

- 완전 함수 종속 : 기본키의 부분집합이 결정자가 되어선 안됨을 의미 ( ==  기본키중에 특정 컬럼에만 종속된 컬럼(부분적 종속)이 없어야 한다.)

- | TABLE1 | COMPANY_ID | NAME  | MAJOR | DEPARTMENT | PROJECT |
  | ------ | ---------- | ----- | ----- | ---------- | ------- |
  |        | B001       | HOSE  | IE    | BACKEND    | PRJ007  |
  |        | B001       | HOSE  | ST    | BACKEND    | PRJ156  |
  |        | D003       | LINA  | SE    | DEVOPS     | PRJ001  |
  |        | F016       | JAMES | ST    | FRONTEND   | PRJ999  |
  |        | F099       | SSAFY | EE    | FRONTEND   | PRJ007  |
  
  위와 같은 회사 사원 목록 테이블이 있고, 해당 테이블은 사원의 정보와 부서, 맡은 프로젝트를 나타낸다.

- `COMPANY_ID`와 `PROJECT`를 기본키로 볼 수 있다.(두 개 조합은 유일하므로)
  
  - 두 개 조합으로 로우를 구분할 수 있지만, 사원의 이름과 부서는 `COMPANY_ID`에 종속되어 있어 중복 데이터가 보인다. 
  
  - 이러한 사항은 테이블을 분리하여 효율적으로 운용할 수 있다.
  
  | TABLE2 | COMPANY_ID | NAME  | DEPARMENT |
  | ------ | ---------- | ----- | --------- |
  |        | B001       | HOSE  | BACKEND   |
  |        | D003       | LINA  | DEVOPS    |
  |        | F016       | JAMES | FRONTEND  |
  |        | F099       | SSAFY | FRONTEND  |
  
  | TABLE3 | COMPANY_ID | PROJECT |
  | ------ | ---------- | ------- |
  |        | B001       | PRJ007  |
  |        | B001       | PRJ156  |
  |        | D003       | PRJ001  |
  |        | F016       | PRJ999  |
  |        | F099       | PRJ007  |
  
  - `COMPANY_ID`가 기본키가 되고 나머지 컬럼들은 그에 종속됨을 확인 할 수 있다.

#### 제3 정규화

> 제2 정규화를 진행한 테이블에 대해 **이행적 종속** 을 없애도록 테이블을 분해하는 것

- 이행적 종속 : A->B, B -> C가 성립할 때, A->C가 성립됨을 의미한다.

- 위 `TABLE3`를 조금 변형시킨 `TABLE4`이다.
  
  | TABLE3 | COMPANY_ID | PROJECT | PAYMENT |
  | ------ | ---------- | ------- | ------- |
  |        | B001       | PRJ007  | 10000   |
  |        | B001       | PRJ156  | 20000   |
  |        | D003       | PRJ001  | 15000   |
  |        | F016       | PRJ999  | 99999   |
  |        | F099       | PRJ007  | 10000   |
  
  `COMPANY_ID`는 `PROJECT`를 결정하고, `PROJECT`는 `PAYMENT`를 결정한다. **연쇄적인** 관계가 보인다. 이러한 상황에서는 `PROJECT`가 여러번 나올때마다 `PAYMENT`가 중복된다. 
  
  - 또한 특정 프로젝트의 보상이 수정해야 한다면, 모든 특정 `PROJECT`의 `PAYMENT`를 모두 찾아서 수정해야하므로, 이는 매우 비효율적이다.

- 따라서 연쇄적인 관계를 끊어내도록 테이블을 분할한다.
  
  | TABLE3-1 | COMPANY_ID | PROJECT |
  | -------- | ---------- | ------- |
  |          | B001       | PRJ007  |
  |          | B001       | PRJ156  |
  |          | D003       | PRJ001  |
  |          | F016       | PRJ999  |
  |          | F099       | PRJ007  |
  
  | TABLE3-2 | PROJECT | PAYMENT |
  | -------- | ------- | ------- |
  |          | PRJ007  | 10000   |
  |          | PRJ156  | 20000   |
  |          | PRJ001  | 15000   |
  |          | PRJ999  | 99999   |
  
  두 테이블은 A->B, B->C의 형식을 갖지만, C의 수정이 필요할때, A->B의 테이블을 Full scan하여 특정 `PROJECT`를 찾는게 아닌, `TABLE3-2`에 1개 행만 찾아 수정하면 된다.

#### BCNF 정규화(Boyce and Codd Normal Form Normalization)

> 제3 정규화를 진행한 테이블에 대해 모든 결정자가 후보키가 되도록 테이블을 분해하는 것.

- 아래 테이블을 봐보자.
  
  | TABLE3-1 | COMPANY_ID | PROJECT | SUPERVISOR |
  | -------- | ---------- | ------- | ---------- |
  |          | B001       | PRJ007  | Mr.P       |
  |          | B001       | PRJ156  | Mr.S       |
  |          | D003       | PRJ001  | Mr.H       |
  |          | F016       | PRJ999  | Mr.J       |
  |          | F099       | PRJ007  | Mr.P       |
  
  위 테이블에서 `COMPANY_ID`와 `PROJECT`는 기본키이자 후보키이다. 기본키로 담당자 `SUPERVISOR`를 결정한다.
  
  하지만 또 `SUPERVISOR`는 `PROJECT`를 결정한다. 하지만 `SUPERVISOR`는 후보키가 아니다.

- `SUPERVISOR`가 담당하는 `PROJECT` 수정이 필요할 경우 위 테이블에서는 갱신 이상이 발생한다. 따라서 결정자가 후보키가 되도록 분리한다.
  
  | TABLE4 | PROJECT | SUPERVISOR |
  | ------ | ------- | ---------- |
  |        | PRJ007  | Mr.P       |
  |        | PRJ156  | Mr.S       |
  |        | PRJ001  | Mr.H       |
  |        | PRJ999  | Mr.J       |
  
  | TABLE3-1 | COMPANY_ID | PROJECT |
  | -------- | ---------- | ------- |
  |          | B001       | PRJ007  |
  |          | B001       | PRJ156  |
  |          | D003       | PRJ001  |
  |          | F016       | PRJ999  |
  |          | F099       | PRJ007  |

---

- 레퍼런스

> [데이터베이스 정규화 1NF, 2NF, 3NF, BCNF :: Deep Play](https://3months.tistory.com/193)
> 
> [[Database] 정규화(Normalization) 쉽게 이해하기 - MangKyu's Diary](https://mangkyu.tistory.com/110)
> 
> [[Database] 7. 정규화(Normalization) - MangKyu's Diary](https://mangkyu.tistory.com/28)
> 
> [데이터베이스 정규화 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EC%A0%95%EA%B7%9C%ED%99%94)
> 
> [함수 종속 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%ED%95%A8%EC%88%98_%EC%A2%85%EC%86%8D)
> 
> [[관계형 데이터베이스] - 함수 종속성 (Functional Dependency)](https://untitledtblog.tistory.com/125)
