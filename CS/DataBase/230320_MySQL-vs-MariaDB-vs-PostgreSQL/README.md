- TOC

---

# MySQL vs MariaDB vs PostgreSQL

## MySQL, MariaDB 그리고 PostgreSQL 비교

- 프로젝트를 시작할때 기술 선택은 설계 과정에서 지나칠 수 없다. 프로젝트를 하면서 `MariaDB`를 2번정도 사용했지만 `MySQL`, `MariaDB` 그리고 `PostgreSQL`간의 차이점에 대해 고려해본 적이 없으므로 오늘은 그 차이점에 대해 알아보겠다.
  - `MySQL`과 `MariaDB`의 차이점에 대해 기술할려 했으나, `PostgreSQL`도 같이 비교하면 좋을 것 같아 추가했다.

### 다양한 오픈 소스 `DB`

- 90년대 중반에 개발된 `MySQL`은 시장에서 사용 가능한 최초의 오픈 소스 `DB`중 하나인 관계형 데이터베이스 관리 시스템(`RDBMS`, Relational DBMS)이다.

- `MariaDB`는 `MySQL`의 개발자인 Monty Widenius가 `MySQL`이 기업에 넘어간 이후 불투명한 오픈 소스 정책에 반발하여 `MySQL` 커뮤니티 버전을 fork하여 새롭게 개발되었다.
  
  - [MariaDB 개요](https://github.com/seho27060/TIL/tree/master/MariaDB)

- `PostgreSQL`은 Micheal Stonebraker의 개발한 `Ingres`가 시초가 되며 `RDBMS`와 구분되는 객체 관계형 데이터베이스 관리 시스템(`ORDBMS`)이다.
  
  - [PostgreSQL 개요](https://github.com/seho27060/TIL/tree/master/PostgreSQL)

### `DB`간 차이점

- `MySQL` vs `MariaDB`와 `MariaDB` vs `PostgreSQL`로 구분하여 살펴보자.

#### `MySQL` vs `MariaDB`

- 기본적으로 `MariaDB`는 `MySQL`에서 시작되었기에 큰 차이를 보이진 않지만, `MariaDB`가 많은 추가 기능을 제공하며 `MySQL`보다 투명한 오픈소스 정책으로 갈수록 발전하고 있다.
  
  - 스토리지 엔진(Storage Engine)상에도 차이점이 있다.

- 기능상의 차이는 아래 표와 같다.
  
  | 용도                 | MySQL                                        | MariaDB                                                                  |
  | ------------------ | -------------------------------------------- | ------------------------------------------------------------------------ |
  | 쓰레드 풀(Thread Pool) | 엔터프라이즈(상용) 버전에서 지원                           | `MariaDB` 5.1 버전 부터 지원                                                   |
  | 버퍼풀 프리로드           | `MySQL` 5.6 버전 부터 `InnoDB` 버퍼풀의 덤프와 로딩 기능 지원 | `XtraDB`에서 버퍼 풀의 내용 덤프, 덤프된 버퍼 풀 정보를 `MariaDB` 재시작 후 다시 버퍼 풀로 로딩하는 기능 제공 |
  | SSD 지원             |                                              | `XtraDB` 에서는 SSD 기반의 디스크 IO를 위한 블록 플러시 알고리즘 지원                           |
  | 반 동기화 애플리케이션       | 플러그인  형태로 제공                                 |                                                                          |
  | 가상 컬럼              |                                              | 1개 이상의 컬럼 값을 미리 별도의 컬럼에 저장하거나 쿼리 처리 시점에 가공하여 보여주는 기능                     |
  | 동적 컬럼              |                                              | NoSQL 처럼 사용할 수 있는 기능                                                     |

- 성능 상의 차이는 `MariaDB` 커뮤니티에서는 `MariaDB`가 월등하다고 주장하고 있다.

- 기능과 성능 외에서 `MariaDB`를 사용하는 경우가 많은데, 이러한 경우는
  
  1. 투명한 오픈 소스 정책과 그로 인한 다양한 레퍼런스
  
  2. 커뮤니티 버전과 엔터프라이즈(상용) 버전이 제공되는 `MySQL`과 다르게 `MariaDB`는 모든 기능을 커뮤니티 기능에 제공하여 누구나 비용없이 사용가능하다.
  
  3. `MariaDB`의 비교적 적은 사용 비용으로 작은 프로젝트에 사용된다.

- `MySQL`과 `MariaDB`를 비교했을때 일반 사용자가`MariaDB`가 갖는 장점은 아래와 같다.
  
  - 동일 하드웨어 사양으로 `MySQL`보다 향상된 성능
  
  - 활성화된 `MariaDB` 커뮤니티
  
  - 비용없이 사용가능한 다양한 기능과 다양한 스토리지 엔진
  
  - 빠르고 투명한 보안패치 릴리즈

#### `MySQL, MariaDB` vs `PostgreSQL`

- `RDBMS`에도 충분히 서비스 구현이 가능할 거 같은데 왜 많은 기업에서는 `PostgreSQL`로 데이터베이스를 구성할까?

- 가장 큰 차이점은 `PostgreSQL`은 **멀티 프로세스** 방식이며, `MariaDB`는 **멀티 쓰레드** 방식을 사용한다는 점이다.
  
  - 멀티 프로세스를 사용하는 `PostgreSQL`은 복잡한 쿼리나 `JOIN`의 처리 방식에서 더 뛰어난 성능을 보인다.
  
  - 아무래도 멀티쓰레드 방식인 `MariaDB`는 복잡한 작업에 1개의 코어가 사용되므로 성능 저하를 불러일으킬 수 있다.
  
  |                       | PostgreSQL                                                                                                                      | MariaDB                                                           |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
  | 방식                    | Multi Processes                                                                                                                 | Multi Threads                                                     |
  | 성능                    | 복잡한 쿼리에 적합하다.<br/>하드웨어의 I/O 속도가 받춰줘야 하며, 광범위한 데이터 분석, `DW`, 데이터 분석 응용 부분에 뛰어난 성능을 보인다.<br/>Disk I/O가 많은 편으로 HDD보다 SSD 환경이 적합하다. | 단순한 데이터 트랜잭션에 뛰어나다.<br/>OLTP/OLAP 시스템에서 읽기 속도만 필요한 경우 좋은 성능을 보인다. |
  | SQL Compliance        | 완전한 Core 적합성을 위한 179개 중 최소 160개를 준수한다.                                                                                          | 비교적으로 적은 개수를 준수한다.                                                |
  | ACID                  | ACID를 지향하며 모든 요구사항을 만족한다.                                                                                                       | `InnoDB`를 사용한 경우만 만족한다.                                           |
  | High Availability     | Master - Slave 구조로, M-S-S 3노드 구성을 권장                                                                                            | 갈레라 클러스터를 이용한 Master - Master 구성 방식으로 3노드를 권장                     |
  | Programming Languages | DB 단에서 `C/C++`, `Java`, `JavaScript`, `R`, `Python` 등 다양한 프로그래밍 언어를 지원한다.                                                       | 지원하지 않는다.                                                         |

- 일반적으로 `PostgreSQL`은 더 큰 규모의 비즈니스에서 복잡한 쿼리를 사용하는 OLTP 환경 또는 저장 데이터를 분석하고 응용하는 OLAP 환경에서 선택된다.
  
  - `MariaDB`나 `MySQL`에 비해 레퍼런스가 적고, 운영에 어려운 점도 있으며 클라우드 환경에서 Scale-out하기 어렵다.

- `MariaDB`는 단순한 트랜잭션 처리를 위한 OLTP/OLAP 환경에 유용하며, 웹 기반의 서비스 용도에 적합하다.

- 두 `DB` 오픈 소스는 각각의 장단점이 있으므로 서비스의 구조, 환경, 목적에 따라 적합한 기술을 선택하여 적용해야 한다.

---

- 레퍼런스

> https://velog.io/@chois90/mariadb-mysql-%EB%B9%84%EA%B5%90%EC%9A%B0%EC%9C%84%EA%B0%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80
> 
> [PostgreSQL과 MariaDB의 사이에서의 선택 - RastaLion&#039;s IT Blog](https://rastalion.me/postgresql%EA%B3%BC-mariadb%EC%9D%98-%EC%82%AC%EC%9D%B4%EC%97%90%EC%84%9C%EC%9D%98-%EC%84%A0%ED%83%9D/)
