- [Consistency and Intergrity](#consistency-and-intergrity)
  - [정합성과 무결성](#정합성과-무결성)
      - [훼손 예시](#훼손-예시)
        - [무결성 훼손](#무결성-훼손)
        - [정합성 훼손](#정합성-훼손)
    - [정합성(Consistency)](#정합성consistency)
    - [무결성(Intergrity)](#무결성intergrity)
      - [무결성 제약조건(Intergrity Constraint)](#무결성-제약조건intergrity-constraint)
        - [개체 무결성(Entity Integrity)](#개체-무결성entity-integrity)
        - [참조 무결성(Referential Integrity)](#참조-무결성referential-integrity)
        - [도메인 무결성(Domain Integrity)](#도메인-무결성domain-integrity)
        - [`NULL` 무결성(Null Integrity)](#null-무결성null-integrity)
        - [고유 무결성(Unique Integrity)](#고유-무결성unique-integrity)
        - [키 무결성(Key Integrity)](#키-무결성key-integrity)
        - [관계 무결성(Relationship Integrity)](#관계-무결성relationship-integrity)
      - [무결성 제약조건의 장단점](#무결성-제약조건의-장단점)
        - [장점](#장점)
        - [단점](#단점)

---

# Consistency and Intergrity

## 정합성과 무결성

- 보다 좋은 데이터베이스 운용을 위해 `DB`의 설계 단계에서 고려해야할 데이터의 정합성과 무결성에 대해 알아보자. 

#### 훼손 예시

##### 무결성 훼손

- 학생 번호는 모두 `-1`로 초기화

- 학생들의 수강 신청에 학생 번호는 `-1`로 입력된다.

- 학생 번호는 양수의 값을 가져야 하며 중복되는 값을 갖지 않아야 한다.

##### 정합성 훼손

- 무결성 훼손을 방지하기 위해 학생 번호를 모두 유일한 값으로 갱신했다.

- 하지만 학생들의 수강 신청 정보의 학생 번호는 갱신되지 않았다.

- 수강 신청 정보로 학생 정보를 조회할 때, 갱신되지 않는 정보로 정확한 학생 정보를 조회할 수 없다.

### 정합성(Consistency)

> 데이터가 서로 모순없이 일관된게 일치하는 상태

- 두 사용자가 동일한 정보로 특정 데이터를 조회했을때, 조회된 두개의 결과에서 데이터의 상태가 서로 일치함을 의미한다.

- 정규화가 이뤄지지 않은 테이블에서 중복데이터의 발생으로 이상현상(anomaly)가 발생할 경우 정합성을 만족하지 못한다.

- 어떤 데이터의 경우 **정합성은 만족하나 무결성은 훼손**될 수 있다.

### 무결성(Intergrity)

> 데이터베이스의 저장 데이터가 `정확성`, `일관성`, `유효성`을 만족하는 상태

- 데이터의 무결성 유지는 `DBMS`의 중요한 기능이다.
  
  - 주로 데이터에 적용되는 제한을 두는 **제약 조건**을 통해 무결성을 유지한다.

- `DB` 설계시에 무결성을 고려하지 않을 경우 중복 데이터, 부모-자식 데이터간의 비논리적 관계가 발생하며 이러한 문제는 잦은 에러와 설계를 다시 고쳐야하는 문제를 야기한다.

#### 무결성 제약조건(Intergrity Constraint)

> 데이터베이스의 `정확성`, `일관성`을 보장하기 위해(무결성 보장) 저장, 삭제, 수정 등을 제약하기 위한 조건

- 제약조건을 통해 데이터의 무결성을 유지한다.

##### 개체 무결성(Entity Integrity)

> 기본 키 제약(Primary Key Constraint)라고도 하며, 테이블은 기본키를 지정하고 그에 따라 지켜야 하는 조건

1. 기본 키에는 `NULL` 값이 올 수 없다.

2. 기본 키는 테이블 내에 오직 하나의 값만 존재한다.(유일성)

##### 참조 무결성(Referential Integrity)

> 외래 키 제약(Foreign Key Constraint)라고도 하며, 테이블 간의 참조 관계를 선언하는 조건

1. 외래 키의 값은 `NULL`이거나 참조하는 관계의 기본키 값과 동일해야 한다.

2. 외래 키 속성은 참조 가능한 값을 가져야 한다.
   
   - 외래 키 속성 값은 상위 테이블 인스턴스에 존재하거나 존재하지 않아(`NULL`)야한다

##### 도메인 무결성(Domain Integrity)

> 테이블에 존재하는 필드의 무결성을 보장하기 위한 조건

- 필드의 타입, `NULL`값 허용(`Nullable`) 등에 대한 사항을 정의하며, 올바른 데이터가 입력되었는지 확인한다.

##### `NULL` 무결성(Null Integrity)

> 테이블의 특정 속성 값이 `NULL`이 될 수 없게 하는 조건

##### 고유 무결성(Unique Integrity)

> 테이블의 특성 속성에 대해 각 레코들이 갖는 값들이 서로 달라야 하는 조건

##### 키 무결성(Key Integrity)

> 하나의 테이블에는 적어도 하나의 키가 존재해야 하는 조건

##### 관계 무결성(Relationship Integrity)

> 테이블의 어느 한 레코드의 삽입 가능 여부 또는 테이블  간 레코드들 사이 관계에 대한 적절성 여부를 지정하는 조건

#### 무결성 제약조건의 장단점

##### 장점

- 스키마 정의 시에 일관성 조건을 한번만 명시함으로, 데이터베이스가 갱신될 때 `DBMS`가 자동으로 일관성 조건을 검사한다.

##### 단점

- 잘못된 설계에 의한 비용이 크다.

- 프로그래밍 작업이 복잡해지며, 무결성 제약조건을 반복해서 구현해야한다.

- 무결성 제약조건 간 충돌이 발생할 수 있다.

---

- 레퍼런스

> [[Database] 데이터 무결성(Data Integrity)이란? :: 코딩 공부 일지](https://cocoon1787.tistory.com/778)
> 
> [[관계형 데이터베이스] - 무결성 (Integrity)](https://untitledtblog.tistory.com/123)
> 
> https://velog.io/@alicesykim95/DB-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AC%B4%EA%B2%B0%EC%84%B1
