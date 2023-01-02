[TOC]

# Database Sharding

## 데이터베이스 샤딩

### Sharding

- 큰 데이터 셋을 더 작고 관리하기 쉬운 여러 단위로 나누는 것

#### 장점과 단점

- 장점
  
  - 샤딩을 통해 데이터를 분할하여 다른 머신에서 데이터를 사용할 수 있다
  
  - 샤딩으로 분할된 데이터는 메모리에 저장할 수 있으므로 대기 시간(Latency)를 단축할 수 있다.
  
  - 여러개의 샤드에 있는 데이터에 대한 트랜잭션 작업으로 데이터를 병렬적으로 처리할 수 있다.
  
  - 샤딩을 통해 데이터베이스 인스턴스를 추가하여 수평적 확장이 가능하다.
  
  - 확장된 데이터베이스 중 1개가 이상이 생겨도 서로 독립적이므로 고가용성(High Availability)를 갖는다.

- 단점
  
  - 여러 샤드에 있는 레코드들을 다루어야 해서 작업이 훨씬 복잡해진다.
  
  - 경쟁 상태(race condition)을 방지하고 데이터 일관성을 보장하는 동시성 제어(Concurrency Control)도 중앙 집중식 데이터베이스에서보다 훨씬 어렵고 비용이 많이 든다.
    
    - 중앙 집중식 데이터베이스의 경우 트랜잭션은 단일 프로세스를 Locking하여 동시엉을 제어할 수 있다.
    
    - 분산 SQL DB의 트랙잭션은 간단한 쿼리도 분산 트랜잭션이 되거나 복잡한 오류나 성능 저하가 일어나기 쉽다.
  
  - 이와 같은 단점으로 일부 분산 관계형 데이터베이스는 샤딩 자동화를 지원하지 않고 일반적으로 확장하기 매우 힘들다.
    
    - 비관계형 데이터베이스가 각광받는 이유.
    
    - NoSQL에서는 일반적인 SQL 데이터베이스에서 보장하는 ACID 보장하지 않는다.

#### SQL과 Nosql의 샤딩

- SQL의 샤딩(Sharding)
  
  - 수직 샤딩(Vertical Sharding) - 데이터 테이블에서 수직으로 분할하여 작은 단위(Chunk)로 나눔
  
  - 수평 샤딩(Horizontal Sharding) - 데이터 테이블을 레코드의 하위 내용을 포함하도록 행단위로 나눔. **확장성이 높아 수직 샤딩보다 적합함**

- Nosql의 샤딩(Sharding)
  
  - 이미 분리된 레코드를 그룹으로 묶어 각 그룹을 다른 샤드에 배치한다.

- SQL과 Nosql의 샤딩으로 분할된 작은 단위(Chunk)는 샤드라고 하는 여러 데이터베이스 인스턴스에 있을 수 있다.
  
  - 각 데이터베이스 샤드에는 여러 레코드 단위가 있을 수 있다.

#### Sharding Strategies

- 샤딩은 일반적으로 레코드 키를 기반으로 수행된다.
  
  - 레코드 키를 기반으로 어떤 샤드에서 기존 레코드를 찾고
  
  - 어떤 샤드에 새로운 레코드를 추가할 수 있다.
  
  - 이때 레코드 키는 레코드의 어떤 값이든 선택하여 사용할 수 있다.
1. Hash Based Sharding(해시 기반 샤딩)
   
   - 레코드 키에 해시 함수를 적용
     
     - 해시 함수는 레코드가 속한 샤드를 결정하는 숫자 값을 생성함
   
   - 모든 샤드에 고르게 레코드를 저장할 수 있으나
   
   - 비슷한 키 값을 갖는 레코드들이 같은 샤드에 속하지 않을 가능성이 크다.

2. Range Based Sharding(범위 기반 샤딩)
   
   - 키스페이스(keyspace)를 여러 근접한 범위로 나눈다.
   
   - 키 값이 비슷한 샤드에 배치되므로 범위 기반 쿼리(Range based queries)에 훨씬 효율적이다.
   
   - 키스페이스가 특정 범위에 몰려있으면 데이터 분포가 고르지 않다.
     
     - 지속적으로 범위를 재조정하는 방안이 필요하다.

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)