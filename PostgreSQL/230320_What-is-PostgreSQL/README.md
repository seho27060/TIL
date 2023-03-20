[TOC]

# PostgreSQL

## What is PostgreSQL?

> **PostgreSQL**은 확장 가능성 및 표준 준수를 강조하는 [객체-관계형 데이터베이스 관리 시스템](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_%EA%B4%80%EA%B3%84_%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4 "객체 관계 데이터베이스")(ORDBMS)의 하나이다. - 위키백과

- `MySQL`과 더불어 시장에서 많이 사용하는 오픈소스 `DB`중 하나인 `PostgreSQL`
  
  - **"free and open source"** 하므로 확장 가능하다.
  
  - 커스텀 데이터 타입, 사용자 정의 함수를 서로 다른 프로그래밍 언어로 데이터베이스 recompliling없이 생성 가능하다. - `PostgreSQL` 공식 문서

- 관계형 `DBMS`에서 파생된 **객체 관계형 데이터베이스 관리 시스템**(`ORDBMS`)로 기본 기능인 `Transaction`과 `ACID`를 지원한다.

- 멀티 프로세스로 작동하는 특징과 같이 `MySQL`과 구분되는 특징이 있다.

### 구조

- **"클라이언트/ 서버 모델"** 을 사용하며 **멀티 프로세스**로 작동한다.

- 서버는 데이터베이스 파일을 관리하며, 클라이언트에서 들어오는 연결을 수용하며, 클라이언트를 대신하여 데이터베이스 액션을 수행한다.

- 다중 클라이언트 연결을 각 커넥션에 대한 새로운 프로세스를 fork한다.
  
  - 클라이언트는 기존 서버와의 간섭없이 새로 생성된 서버 프로세스와 통신한다.

### 특장점

#### 유연한 객체 생성

- 연산자, 복합 자료형, 집계 함수, 자료형 변환자, 확장 기능 등 다양한 데이터베이스 객체를 사용자가 임의로 만들 수 있는 기능을 `SQL`차원에서 제공한다.

#### 상속

- `Java`, `C++`와 같이 테이블(`Template`)를 만들어 테이블 상속 기능을 이용하여 하위 테이블을 만들 수 있다.
- 테이블에 저장된 자료는 상위 테이블을 조회시, 해당 테이블의 하위 테이블의 자료를 조회할 수 있다.
- 상위 테이블을 그대로 상속받아 새로운 컬럼을 갖는 하위 테이블을 생성할 수 도 있다.

#### 함수

- "저장 프로시저"라고 불리는 `SQL`문으로 작성된 함수를 서버 환경에서 사용할 수 있다.

- 제어문과 반복문을 사용할 순 없지만 다른 언어와 결합 가능하다.
  
  - `PL/pgSQL`, 스크립트 언어(`PL/Python`, `PL/php`..), 컴파일 언어(`C/C++, PL/Java`), 통계적 언어(`PL/R`)

#### 내부 기능

#### `Template` 데이터베이스

- `PostgreSQL`에서는 `CREATE Database`로 테이블을 생성할 때, 기본으로 생성된 `Template1 Database`를 복사하여 생성한다.
  
  - `Template Database`는 표준 시스템 데이터베이스로 원본 데이터베이스에 해당한다.

- `Template0`라는 2차 표준 시스템 데이터베이스가 있으며, 이는 `Template1`의 초기 내용과 동일한 데이터가 포함된다.
  
  - `Template0`은 수정하지 않고 원본 그대로 유지하여 무수정 상태의 데이터베이스를 생성할 수 있다.

- 일반적으로 `Template1`에는 인코딩, 로케일과 같은 설정을 하고, 템플릿을 복사하여 데이터베이스를 생성한다.
  
  - `Template0`을 통해 새로운 인코딩 및 로케일 설정을 지정할 수 있다.
  
  - ```sql
    CREATE DATABASE dbname TEMPLATE template0;
    ```
    
    위와 같이 템플릿으로 데이터베이스를 생성한다.

#### `Vacuum`

- `Vacuum`은 `PostgreSQL`에만 존재하는 고유 명령어로, 오래된 영역을 재사용하거나 정리해주는 명령어이다.

- `PostgreSQL`은 **MVCC(Multi-Version Concurrency Control, 다중 버전 동시성 제어)** 기법을 활용하므로 특정 Row를 추가, 수정할 경우 디스크 상의 Row를 물리적으로 업데이트하지 않고 **새로운 영역을 할당**해서 사용한다.
  
  - `UPDATE`, `DELETE`, `INSERT`와 같은 `DML`이 자주 발생하는 `DB`의 경우 물리적인 저장 공간이 삭제되지 않고 남아있게 되므로, `VACUUM`을 통해 주기적으로 정리하는게 좋다.

---

- 레퍼런스

> [PostgreSQL - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/PostgreSQL)](https://ko.wikipedia.org/wiki/MariaDB)
> 
> [NAVER D2](https://d2.naver.com/helloworld/227936)
> 
> https://www.postgresql.org/about/
> 
> [[PostgreSQL] PostgreSQL이란? - MangKyu's Diary](https://mangkyu.tistory.com/71)
