[TOC]

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

### [데이터베이스 샤딩(Database Sharding)]()

### NoSQL Database Advantages and Disadvantages

- 일부 NoSQL 데이터베이스들은 여러 레코드들이 동일한 물리적 노드에 있는 경우에만 그 레코드들을 사용하는 작업의 원자성을 보장한다.

- 일부 NoSQL 데이터베이스는 일관성을 보장하지 않는다.

- 어떤 경우에는 여러 레코드를 다루는 작업의 원자성도 보장하지 않는다.

- NoSQL 데이터베이스가 샤딩과 확장에 용이하지만, 시스템을 설계하기는 매우 까다롭다.

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
