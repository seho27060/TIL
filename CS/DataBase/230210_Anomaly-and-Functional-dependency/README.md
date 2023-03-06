- [Anomaly and Functional Dependency](#anomaly-and-functional-dependency)
  - [이상현상과 함수 종속성](#이상현상과-함수-종속성)
    - [이상현상(Anomaly)](#이상현상anomaly)
      - [삽입 이상(Insertion Anomaly)](#삽입-이상insertion-anomaly)
      - [갱신 이상(Update Anomaly)](#갱신-이상update-anomaly)
      - [삭제 이상(Delete Anomaly)](#삭제-이상delete-anomaly)
    - [함수 종속성(Functional Dependency)](#함수-종속성functional-dependency)

---

# Anomaly and Functional Dependency

## 이상현상과 함수 종속성

- 관계형 `DB`를 설계, 운용할 때 고려해야할 사항인 **이상현상(Anomaly)** 와 **함수 종속성(Functional Dependency)** 에 대해 알아보자.

- 잘못된 `DB` 설계로 인해 발생하는 문제로 **정규화** 로 미연에 방지 할 수 있다.

- 아래의 테이블을 예시로 각 개념을 살펴보자.
  
  | TABLE1 | NAME  | MAJOR | DEPARTMENT |
  | ------ | ----- | ----- | ---------- |
  |        | HOSE  | IE    | BACKEND    |
  |        | HOSE  | ST    | BACKEND    |
  |        | LINA  | SE    | DEVOPS     |
  |        | JAMES | ST    | FRONTEND   |
  
  어느 회사의 사원 목록 테이블이며 각각의 컬럼은 이름. 전공, 부서를 의미한다.

### 이상현상(Anomaly)

> 테이블 내의 데이터들이 불필요하게 중복되어 테이블을 조작(삽입, 삭제, 수정)할 때 발생하는 데이터 불일치 현상

- 잘못된 테이블 설계로 발생하는 현상으로 이는 정규화로 해결 할 수 있다.

- 이상현상은 **삽입 이상**, **삭제 이상**, **갱신 이상**들 3가지로 구분된다.

#### 삽입 이상(Insertion Anomaly)

> 불필요한 정보를 함께 저장하지 않고서는 어떤 정보를 저장하는 것이 불가능한 현상

- `CANNY`라는 신입사원이 입사했을때, 부서 배치가 이전인 상태로 `DEPARTMENT`를 `NULL`값으로 할당하지 않는 이상 새로운 레코드를 삽입할 수 없다. 

- | NAME  | MAJOR | DEPARTMENT |
  | ----- | ----- | ---------- |
  | CANNY | ME    | NULL       |
  
  어느 컬럼에 불필요한 정보(`NULL`)가 포함되어 있다.

#### 갱신 이상(Update Anomaly)

> 중복된 데이터 중 일부만  수정되어 무결성을 해치는 현상

- 예시 테이블에서 `HOSE` 사원의 부서 이동으로 `DATA ENGINEERING` 으로 수정될 경우, 다른 중복된 데이터는 수정되지 않아 `HOSE` 사원의 정보를 조회할 경우 서로 다른 `DEPARTMENT`가 출력된다.

- 데이터 일치를 위해서는 다른 `HOSE` 레코드의 `DEPARTMENT` 또한 수정돼야 한다.

#### 삭제 이상(Delete Anomaly)

> 어떤 정보를 삭제하면, 의도하지 않은 다른 정보까지 삭제되는 현상

- 기업의 사업 개편으로 `ST`라는 `MAJOR` 하나만을 갖는 사원을 해고(ㅠㅠ)했을 경우, `IE`와 `ST` 두개 전공을 갖는 `HOSE`까지 삭제된다.

- 이러한 현상은 각각의 사원에 고유한 사원 번호(`COMPANY_ID`)를 할당함으로 해결할 수 있다.

- | TABLE1 | COMPANY_ID | NAME  | MAJOR | DEPARTMENT |
  | ------ | ---------- | ----- | ----- | ---------- |
  |        | B001       | HOSE  | IE    | BACKEND    |
  |        | B001       | HOSE  | ST    | BACKEND    |
  |        | D003       | LINA  | SE    | DEVOPS     |
  |        | F016       | JAMES | ST    | FRONTEND   |
  
  위 와 같이 변경하여 `MAJOR`가 `ST`하나뿐인 사원 `LINA`의 `COMPANY_ID`인 `D003`의 레코드를 삭제한다.

### 함수 종속성(Functional Dependency)

> 어떤 속성 A의 값을 알면 다른 속성 B의 값이 유일하게 정해지는 관계
> 
> A -> B 와 같이 표현하며 이때 A를 B의 결정자(Deteminant)라 한다.

- 테이블예시와 같이 사원 번호(`COMPANY_ID`)로 사원 이름(`NAME`)은 의존 관계라 할 수 있다.
  
  - 이때 `NAME`은 `COMPANY_ID`에 종속(Dependant)이다.
  
  - 또는 `COMPANY_ID`는 `NAME`을 결정(Determine)한다.

---

- 레퍼런스

> [인덱스 (데이터베이스) - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%9D%B8%EB%8D%B1%EC%8A%A4_(%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4))
> 
> [데이터베이스 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4)
> 
> [[DB] 데이터베이스(DB) 인덱스(Index) 란 무엇인가?](https://choicode.tistory.com/27)
