- [Distributed\_System\_08](#distributed_system_08)
  - [분산형 메시지 브로커 - 01](#분산형-메시지-브로커---01)
      - [메시지 브로커의 필요성](#메시지-브로커의-필요성)
    - [Message Broker](#message-broker)
      - [메시지 브로커 특징](#메시지-브로커-특징)
    - [Apache Kafka](#apache-kafka)
      - [카프카의 추상화 계층](#카프카의-추상화-계층)
      - [Consumer](#consumer)
    - [분산 시스템에서의 카프카](#분산-시스템에서의-카프카)
      - [Kafka Perfomance and Scalability](#kafka-perfomance-and-scalability)
        - [카프카 브로커와 Topic Partitions](#카프카-브로커와-topic-partitions)
        - [Cunsumers and Topic Partitions](#cunsumers-and-topic-partitions)
        - [Topic Partitions and Parallelism](#topic-partitions-and-parallelism)
      - [Kafka Fault Tolerance](#kafka-fault-tolerance)
        - [Replication - Leader \& Followers](#replication---leader--followers)
      - [Data Persistence in Kafka](#data-persistence-in-kafka)


# Distributed_System_08

## 분산형 메시지 브로커 - 01

#### 메시지 브로커의 필요성

- 직접 네트워크 통신의 특징 중

- Synchronous Network Communication(동기식 통신)
  
  - 클라이언트와 서버의 연결이 필수적
  
  - 사용자가 상품을 구매할때 주문 - 결제 - 배송 - 확인 이라는 4개의 서비스는 서로 **종속되어 연결**되어 있음. 

- Broadcasting Event to Many Services(어떤 작업(event)가 여러 서비스에 요청)
  
  - 각 서비스마다 연결을 맺어야함
  
  - 확장성이 없음

- Traffic Peaks and Balleys(예상못한 트래픽 급증)

### Message Broker

- 송신자와 수신자사이에서 메시지를 전달하는 중개자 역할의 소프트웨어 구성 요소를 사용하는 소프트웨어 패턴

- 메시지 전달뿐만 아니라 데이터 변환, 검증, 큐잉(queuing), 라우팅 등의 부가기능 제공

- 수신자와 송신자간의 **종속성**이 없다.

#### 메시지 브로커 특징

- Distributed Queue(분산 큐)
  
  - Queueing을 활용하여 동기식 통신을 비동기식 통신으로 변환할 수 있다.

- Publish/Subscribe(발행/구독) 모델
  
  - 발행자(송신자)가 메시지를 송신하면 메시지 브로커가 구독자(수신자)에게 자동으로 메시지를 전달한다.
  
  - 이때 송신자와 수신자는 누구에게 보내야하는지, 누구에게 받는지와 같은 정보가 필요없다.

- Push vs Pull
  
  - 기존의 직접 네트워크 통신에서는 클라이언트가 서버에 메시지를 보낼때(push) 서버는 메시지 수신에 대한 제어권이 없어 받기만 한다.
  
  - 메시지 브로커를 활용할 경우 클라이언트는 메시지를 브로커에 보내고(push) 서버는 메시지를 수신(pull)하여 메시지에 대한 제어권을 얻게 된다.

- 단일 실패 지점(Single point of failure)나 병목(bottleneck) 현상을 피하기 위해 확장성(scalable)과 내결함성(fault tolerant)을 가져야 한다.
  
  - 이를 위해 설계하고 설정하는 건 매우 어려운 일

### Apache Kafka

- 분산 스트리밍 플랫폼으로 서로 다른 서비스간 실시간으로 메시지를 주고받을때 사용한다.

- 내부적으로 분산 시스템이며 메시지를 다루기 위해 다수의 메시지 브로커를 사용한다.

- 범용적인 오픈소스이며 분산 큐와 발행/구독 기능을 모두 제공하며 그 자체로 훌룡하게 설계된 분산시스템이다.

#### 카프카의 추상화 계층

- Producer Record
  
  - 메시지를 카프카에 보내면 Record에 저장된다.
  
  - Record는 Key, Value(메시지), Timestamp로 구성되어 있다.

- Topic 
  
  - 메시지나 이벤트의 묶음
  
  - 퍼블리셔나 서비는 토픽에 이벤트나 메시지를 발행하거나 각 서비스에서는 토픽을 소비한다.
  
  - 카프카는 토픽을 여러개로 분할(Partitioned)하여 관리한다.
    
    - 토픽은 여러개의 파티션으로 구성된다.
    
    - 각 파티션은 개별적인 레코드의 큐이며, 레코드들은 발행 **순서에 따라 큐에 쌓이게 된다**.
    
    - 메시지의 key에 따라 정해진 파티션에 전달된다.
    
    - 많은 파티션은 확장성과 좋은 성능을 갖추게 한다.

#### Consumer

- 카프카 토픽으로부터 메시지를 소비하는 애플리케이션의 인스턴스를 위해 Consumer는 Consumer Group에 소속되어야 한다.

- Consumer가 토픽을 구독(subscribe)하면 각 메시지는 컨슈머 그룹의 개별 인스턴스로 전달된다.

- Distributed Queue에서..
  
  - 토픽에서 그룹으로 메시지가 전달될 경우, 해당 그룹 내의 Consumer모두에게 메시지가 분산되어 전달된다.

- Publish/Subscribe System에서..
  
  - 각각의 컨슈머를 다른 그룹에 두어 모든 컨슈머에게 메시지를 전달한다. ->?

### 분산 시스템에서의 카프카

#### Kafka Perfomance and Scalability

##### 카프카 브로커와 Topic Partitions

- Topic = Partition0 + Partition1 + Partition2 와 같이 여러개의 파티션으로 구성되어 있다.

- 1개의 메시지 브로커에 1개의 토픽을 할당한다면 CPU와 컴퓨터 메모리에 의해 확장이 제한된다.

- 이때 토픽의 파티션을 여러개의 브로커 인스턴스에 배분한다.

- 토픽의 파티션 개수는 
  
  - 카프카 토픽을 위해 구성된 병렬 장치의 최대 개수와 비례한다.
  
  - 또는 메시지가 들어오는 속도와 양을 보고 파티션 개수를 측정한다.

##### Cunsumers and Topic Partitions

- 카프카 브로커에 할당된 토픽의 파티션은 Consumer Group으로 전달된다.

- Consumer Group내에서는 여러개의 Cunsumer로 파티션이 분배되어 작업한다.

##### Topic Partitions and Parallelism

- 토픽의 파티셔닝으로
  
  - 병렬적 브로커 인스턴스를 통해 메시지를 처리할 수 있다.,
  
  - 많은 컨슈머가 동일한 토픽에서 병렬로 소비(consume)할 수 있다.

#### Kafka Fault Tolerance

- 여러개의 카프카 브로커 구성에서, 1개의 브로커의 오류가 생기면 모든 데이터와 해당 브로커에 할당된 파티션을 잃게 된다.

##### Replication - Leader & Followers

- 각각의 카프카 토픽은 복제 횟수(Replication Factor)를 설정할 수 있다.
  
  - 복제 횟수가 클 경우 내결함성을 갖출 수 있지만
  
  - 그만큼 메모리를 많이 사용한다는 뜻이기도 하다.

- 복제 횟수 N은 토픽의 각 파티션이 N개의 카프카 브로커에 복제된다는 뜻이다.
  
  - 복제 횟수가 2일 경우, 모든 파티션의 2개의 브로커에 복제된다.

- 각 파티션마다 하나의 브로커가 리더를 맡고 나머지는 팔로워를 맡는다.
  
  - 리더는 모든 읽기와 쓰기(reads and writes)를 담당하며
  
  - 팔로워는 리더의 모든 데이터를 적극적으로 복제하고 리더에 오류 발생시 언제든 대체 가능하도록 대기한다.
  
  - 리더-팔로워 역할은 주키퍼(zookeeper)를 통해 관리된다.

#### Data Persistence in Kafka

- 카프카는 모든 메시지를 디스크에 유지한다

- 메시지가 컨슈머에의해 소비되어도 레코드는 카프카에 당분간 지속된다.
  
  - 이러한 지속성은 새로운 컨슈머가 오래된 메시지의 기록을 확인할 수 있다.
  
  - 데이터를 잃지 않고 작업을 다시 시도할 수 도 있다.

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
