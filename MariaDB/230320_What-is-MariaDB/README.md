[TOC]

# MariaDB

## What is MariaDB?

> **MariaDB**는 [오픈 소스](https://ko.wikipedia.org/wiki/%EC%98%A4%ED%94%88_%EC%86%8C%EC%8A%A4)의 [관계형 데이터베이스 관리 시스템](https://ko.wikipedia.org/wiki/%EA%B4%80%EA%B3%84%ED%98%95_%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EA%B4%80%EB%A6%AC_%EC%8B%9C%EC%8A%A4%ED%85%9C "관계형 데이터베이스 관리 시스템")(RDBMS)이다. [MySQL](https://ko.wikipedia.org/wiki/MySQL "MySQL")과 동일한 소스 코드를 기반으로 하며, GPL v2 라이선스를 따른다. [오라클](https://ko.wikipedia.org/wiki/%EC%98%A4%EB%9D%BC%ED%81%B4 "오라클") 소유의 현재 불확실한 MySQL의 라이선스 상태에 반발하여 만들어졌으며, 배포자는 [몬티 프로그램 AB](https://ko.wikipedia.org/w/index.php?title=%EB%AA%AC%ED%8B%B0_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8_AB&action=edit&redlink=1 "몬티 프로그램 AB (없는 문서)")(Monty Program AB)와 저작권을 공유해야 한다. - 위키백과

- `MySQL`과 동일한 소스코드를 기반으로 하며, 모든 기능과 API가 `MySQL`과 정확히 매칭하여 높은 호환성을 지닌다.

- Monty Widenius가 `MySQL AB`를 개발하여  Sun Microsystems에 판매하였으나, 기업에서의 비공개로 인한 불투명한 오픈소스 정책에 반발하여 `MariaDB`라는 이름으로 새로운 오픈소스 데이터베이스로 개발되었다.

- `MySQL`의 커뮤니티 버전 오픈소스를 fork하여 개발되었으므로, `MySQL`에서 제공하는 기본 기능을 모두 제공할 뿐만 아니라 추가적인 기능도 제공한다.

### 특징

#### `MySQL`과의 호환성

- `MariaDB`는 `MySQL`과 소스코드를 같이 하므로 **사용방법과 구조**가 `MySQL`과 **동일**하다.

- 이러한 사항은 두개의 오픈소스의 각 버전이 버전별로 완전히 호환되어, 클라이언트 API, 프로토콜 등이 동일하게 사용됨을 확인할 수 있다.

#### 성능

- `MariaDB` 커뮤니티에서는 `MySQL`과 비교하여 애플리케이션 부분 속도가 월등히 빠르다고 주장하고 있다.

#### 기능

- `MySQL`에서 제공하는 **Threadful**기능이 내장되었으며, 스토리지 엔진을 활용한 샤딩 기술도 제공한다.
  
  - 가상 컬럼, Table 제거, 스토리지 엔진 지정, GIS 기능 지원, 멀티 소스 리플리케이션 등 다양한 기능 또한 추가 제공한다.

### 엔진

- `MySQL`과 거의 동일한 데이터베이스 엔진이 대응되며 해당 데이터베이스 엔진은 아래와 같다.
  
  - `Aria`, `XtraDB`, `FederatedX`, `OQGRAPH`, `SphinxSE`,`Cassandra`(!!!..)

---

- 레퍼런스

> [MariaDB - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/MariaDB)
> 
> [MariaDB 와 MySQL - 기능 - MariaDB Knowledge Base](https://mariadb.com/kb/ko/mariadb-vs-mysql-features/)
