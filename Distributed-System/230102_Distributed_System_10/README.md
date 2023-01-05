- [Distributed System 10](#distributed-system-10)
  - [분산형 스토리지 및 데이터베이스](#분산형-스토리지-및-데이터베이스)
    - [분산형 스토리지 소개](#분산형-스토리지-소개)
    - [데이터베이스 샤딩(Database Sharding)](#데이터베이스-샤딩database-sharding)
    - [NoSQL Database Advantages and Disadvantages](#nosql-database-advantages-and-disadvantages)
    - [일관된 해싱을 이용한 동적 샤딩](#일관된-해싱을-이용한-동적-샤딩)
      - [Consistent Hashing(일관된 해싱)](#consistent-hashing일관된-해싱)
    - [데이터베이스 복제, 일관성 모델 및 정족수 합의](#데이터베이스-복제-일관성-모델-및-정족수-합의)
      - [Database Replication(데이터베이스 복제)](#database-replication데이터베이스-복제)
      - [Replicated Database Architectures(복제 데이터베이스 구조)](#replicated-database-architectures복제-데이터베이스-구조)
      - [Database Consistency Models(데이터베이스 일관성 모델)](#database-consistency-models데이터베이스-일관성-모델)
      - [Quorum Consensus(정족수 합의)](#quorum-consensus정족수-합의)


# Distributed System 10

## 분산형 스토리지 및 데이터베이스

- File System
  
  - 데이터의 형식, 구조, 크기에 구애받지 않는 낮은 수준의 범용 저장 방식
  
  - 구조화 데이터가 아니거나 데이터간 관계가 없어도 어떤 데이터든 저장이 가능하다.

- Database
  
  - 높은 수준의 추상화
  
  - 질의엔진(query Engine), 캐싱, 성능 최적화를 제공하는 애플리케이션
  
  - 데이터의 구조, 관계, 형태 등의 제한을 제공한다.
  
  - 전체 시스템은 [ACID 트랜잭션](https://github.com/seho27060/TIL/tree/master/CS/DataBase/220917%20Transaction)을 보장한다. 
  
  - [관계형 데이터베이스(SQL)과 비관계형 데이터베이스(Nosql)](https://github.com/seho27060/TIL/tree/master/CS/DataBase/220902%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EC%A2%85%EB%A5%98)로 나뉜다.

### 분산형 스토리지 소개

- 우리가 데이터베이스에 원하는 기능
  
  - 가용성(Availability)
  
  - 확장성(Scalability)
  
  - 내결함성(Fault Tolerance)

- 중앙 집중식 데이터베이스의 발생 가능한 문제점(Issues)
  
  - 단일 장애점(Single Point of Failure)
    
    - 분산시스템에서 데이터베이스 노드를 잃는 것은 컴퓨팅 노드를 잃는 것보다 더 치명적인 결함을 유발한다.
    
    - 컴퓨팅 노드의 단일 장애로 인한 서비스 중지는 일시적이며 복구 후 정상 가동화가 가능하지만
    
    - 데이터베이스의 단일 장애는 데이터의 영구적 손실로 서비스 작동에 매우 치명적이다.
  
  - 성능 병목(Performance Bottleneck)
    
    - 데이터베이스의 병렬 처리는 해당 머신의 코어 개수로 제한된다.
    
    - 연결 또한 OS와 네트워크 카드에 따라 제한된다.
    
    - 유저와 데이터베이스의 지리적 위치에 따라 최소 대기 시간(Minimum Latency)가 결정된다.
    
    - 메모리 사용 역시 머신의 메모리 용량에 따라 제한된다.

- 분산 스토리지를 통해 위 문제들을 해결해보자..

### [데이터베이스 샤딩(Database Sharding)](https://github.com/seho27060/TIL/tree/master/CS/DataBase/230102_Database-Sharding)

### NoSQL Database Advantages and Disadvantages

- 일부 NoSQL 데이터베이스들은 여러 레코드들이 동일한 물리적 노드에 있는 경우에만 그 레코드들을 사용하는 작업의 원자성을 보장한다.

- 일부 NoSQL 데이터베이스는 일관성을 보장하지 않는다.

- 어떤 경우에는 여러 레코드를 다루는 작업의 원자성도 보장하지 않는다.

- NoSQL 데이터베이스가 샤딩과 확장에 용이하지만, 시스템을 설계하기는 매우 까다롭다.

### 일관된 해싱을 이용한 동적 샤딩

- **Hash Based Sharding Strategy**의 문제
  
  - 해쉬 기반 샤딩에서 레코드는 레코드 키값을 샤드의 개수 N만큼 나눈 나머지 m에 따라 m번째 샤드에 저장한다.
    
    - EX) shard0=key0,key3/shard1=key1,key4/shard2=key2,key,5
    1. 이때 새로운 샤드가 추가되거나, 기존 샤드가 제거될 경우 모든 샤드에 속한 레코드 값은 재배치해야한다.(Dynamic Cluster Resizing)
    2. 노드들 간의 하드웨어 성능 차이로 더 많은 데이터를 좋은 성능의 노드에 저장하고 싶지만, 해쉬 기반 샤딩은 모든 노드에 순차적으로 공평하게 데이터를 분배하므로 불가능하다.(Asymmetric Nodes)

#### Consistent Hashing(일관된 해싱)

- 데이터와 키 값과 데이터가 저장된 데이터베이스 노드를 매핑해서 같은 해시 공간에 저장한다.
  
  - 키와 노드를 원형 고리 모양의 동일한 해시 공간에 둔다.
  
  - 어느 특정 노드 값과 이전 노드 위치 사이의 값을 갖는 모든 키가 그 특정 노드에 속하게 된다 ...?

- **특징**
  
  - 분산형 데이터베이스 노드들에 데이터가 고르게 분포한다.
  
  - 기존의 해쉬 기반 샤딩과 다르게, 너무 많은 키를 다시 할당하지 않고도 클러스터에서 노드를 동적으로 추가하거나 제거할 수 있다.
  
  - 성능이 좋은 노드에 더 많은 키를 할당하고, 그렇지 않은 노드에는 적은 키를 손쉽게 할당할 수 있다.
    
    - 가상 노드(Virtual node)를 성능에 비례하여 배치한다.

- **문제점**
  
  - 부하 분포가 고르지 않을 수 있다.(Uneven Distribution)
    
    - 여러개의 해쉬 함수(Multiple Hash Functions)를 사용하여 해결 할 수 있다.

### 데이터베이스 복제, 일관성 모델 및 정족수 합의

#### Database Replication(데이터베이스 복제)

- 샤딩은 데이터를 분할(Splitting)한 작은 단위(Chunk)를 다른 머신에 저장한다.

- 복제(Replication)은 모든 데이터의 동일한 복사본(Copy)을 만들어 다른 머신에 저장한다.
  
  - 복제의 경우 샤딩과 다르게 중복성(Redundancy)가 있다.

- **특징**
  
  - 고가용성(High Availability)
    
    - 마스터 노드를 서브 노드에 복제했을 경우, 마스터 노드의 연결이 끊어져도 서브 노드에 연결하여 그 역할을 대체할 수 있다.
  
  - 내결함성(Fault Tolerance)
    
    - 마스터 노드가 Shut down되어도 복제된 서브 노드로 대체하여 사용 가능함.
  
  - 확장성과 성능(Scalability/Performance)
    
    - 읽기 집약적 워크로드에 빛을 발한다.
    
    - 엄청나게 많은 읽기 요청(Read Request)를 여러개의 복제된 DB노드에 분할하여 부하를 분담을 할 수 있다.

#### Replicated Database Architectures(복제 데이터베이스 구조)

- **Master-Slave Architecture**
  
  - 쓰기 작업은 모두 마스터에서 하고
  
  - 읽기 작업은 슬레이브에서 한다.
  
  - 마스터의 쓰기 작업은 이후 모든 슬레이브 노드로 전달되어 동일한(Concurrent) 상태를 유지한다.
  
  - 마스터 노드의 Shut down이 발생하면 다른 슬레이브 노드가 마스터의 역할을 대체한다.

- **Master-Master Architecture**
  
  - 마스터 노드가 1개로 모든 쓰기 작업을 감당하기 힘들면 마스터 노드를 여러개로 늘린다.
  
  - 모든 노드가 마스터 노드의 역할을 하며 읽기, 쓰기 작업을 진행한다.
  
  - 모두 같은 상태를 유지하기 위해 1개 마스터 노드의 쓰기 작업은 다른 마스터 노드들에게 전달된다.
  
  - 모든 노드의 역할이 동일하므로 필요한만큼 노드를 확장할수도 있다.

#### Database Consistency Models(데이터베이스 일관성 모델)

- **Eventual Consistency(최종 일관성)**
  
  - Master-Slave 구조에서 마스터 노드의 쓰기 작업중 슬레이브 노드의 읽기 작업이 동시에 일어난다면, **일시적으로(Temporarily)** 일관성을 가질 수 없다. 다만 마스터 노드와 슬레이브 노드의 동기화로 이후 일관성을 갖게된다.
  
  - 업데이트가 없다면 모든 사용자가 최신 데이터를 접근할 수 있지만
  
  - 업데이트가 있다면 어떤 사용자들은 일시적으로 오래된 데이터에 접근한다.
  
  - 전체 클러스터가 업데이트되는걸 기다리지 않고 읽기,쓰기 작업에 응답하기 때문에 대기 시간이 짧고 가용성이 높다(Low Latency and High availability)
  
  - 전반적으로 최신 데이터가 필요하지 않는 소셜미디어 서비스, **분석(Analystics) 서비스**에 적합하다.

- **Strict Consistency(엄격한 일관성)**
  
  - 마스터의 쓰기 작업으로 모든 슬레이브 노드에 데이터를 업데이트한 후 읽기 작업에 응답할 수 있다.
  
  - 엄격하게 일관성을 보장할 수 있지만, 작업 속도가 느려진다.
  
  - 노드 업데이트 전 해당 노드에 읽기 작업이 불가하기 때문에 가용성이 낮다.
  
  - 금융권이나 신뢰성이 중요한 서비스에 적합한 모델이다.
  
  - 마스터-마스터 구조의 엄격한 일관성 모델인 경우, 마스터 노드 1개라도 Shut down되면 엄격한 일관성을 지키기 어렵다. -> 정족수 합의로 해결할 수 있다.

#### Quorum Consensus(정족수 합의)

- 정족수 합의에서는 모든 레코드는 키와 데이터 외에서 버전을 갖는다.
  
  - Record = Key + Data + Version

- 레코드가 업데이트 될때마다 이전 레코드와 새로운 레코드를 구별하기 위해 버전을 늘린다.(Old Record Version = 1, New Record Version = 2)

- **정족수 합의**
  
  - R = 읽기 작업시 사용자가 읽어야 하는 최소 노드 개수
  
  - W = 쓰기 작업시 사용자가 써야 하는 최소 노드 개수
  
  - N = 데이터베이스 클러스터의 모든 노드의 개수
    
    > R + W > N 와 같은 수식을 절대적으로 만족한다면 엄격한 일관성(Strict Consistency)를 지킬 수 있다.
    
    EX) N = 5, R = 3, W = 3 일때,  3 + 3 > 5 라는 수식을 절대적으로 만족한다.

- **특징**
  
  - R, W를 워크로드에 맞게 설정하여 읽기 작업이나 쓰기 작업에 최적화(Optimizing)할 수 있다.
    
    - 과적합(Over Optimizing)은 오히려 읽기 작업과 쓰기 작업의 성능 저하를 불러 일으킨다.
      
      - EX) R = 1, W = 5, N =5 일때 분산 스토리지의 의미가 없어진다.
  
  - 또한 엄격한 일관성을 만족하면서 고가용성을 갖출 수 있다.

- Note : 실제 비관계형 데이터베이스의 경우 샤딩과 복제의 조합으로 고가용성을 유지한다!!

- 정족수 합의 미쳤네..

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
