- [udemy HDFS_05](#udemy-hdfs_05)
  - [HBase](#hbase)
    - [index1](#index1)
      - [detail-index1](#detail-index1)
    - [Kafka](#kafka)
      - [What is streaming?](#what-is-streaming)
      - [Two Problems](#two-problems)
      - [Kafka 활용](#kafka-활용)
        - [Kafka architecture](#kafka-architecture)
    - [YARN](#yarn)
    - [TEZ](#tez)
    - [MESOS](#mesos)
    - [ZOOKEEPER](#zookeeper)
      - [해결가능한 Failuer modes](#해결가능한-failuer-modes)
      - [분산시스템 내의 원시적(Primitive) 실행](#분산시스템-내의-원시적primitive-실행)
      - [ZooKeeper quorums](#zookeeper-quorums)
    - [Oozie](#oozie)
      - [워크플로우 조직하기](#워크플로우-조직하기)
    - [Zeppelin](#zeppelin)

# udemy HDFS_05

## HBase

### index1

#### detail-index1

### Kafka

#### What is streaming?

- 데이터가 생성되는 즉시 클러터에 가져올 수 있다.

- Kafka를 활용하여 HBase, HDFS 등에 저장

- 실시간 주식 거래, 고객 행동 데이터 etc..

#### Two Problems

1. 어떻게 데이터 소스를 클러터스로 가져 올 것인가.

2. 데이터를 가져와서 무엇을 할건가.

#### Kafka 활용

1. Kafka 서버의 클러스터를 구성, 데이터 생성시 서버에 저장

2. 저장됨과 동시에 필요헌 대상에게 발행

##### Kafka architecture

- Producers

- Consumers

- Connectors

- Stream Processors

### YARN

- 하둡 클러스터의 리소스 관리
- 내부적으로 작동함
- 노드를  구분하여 어떻게 분산해 클러스터에 걸쳐 처리할지 결정한다.
  - 또한 네트워크에 의한 데이터 이동을 최소화한다.
- 클러스터 CPU 사용을 최적화하여 **데이터를 최대한 지역적으로 유지**해서 애플리케이션 프로세스가 최대한 빠르게 데이터 블록을 HDFS로 가져올 수 있도록 한다.

#### Yet Another Resource Nagotiator(또다른 리소스 교섭자)

- Cluster Storage Layer인 HDFS위에 Cluster Compute Layer 에 YARN이 위치한다.
  
  - YARN은 클러스터에 **컴퓨팅 작업을 분산**하고
  
  - HDFS는 클러스터에 데이터를 분산해 저장한다.

- YARN 위에 맵리듀스, 스파크가 실행된다.

#### 작동과정

![](C:\Users\seho2\AppData\Roaming\marktext\images\2023-01-07-15-22-48-image.png)

- Client Node에서 실행을 요청받고, YARN(Resource Manager)가 NodeManager에게 작동 요청을 전달

- NodeManager는 YARN과 협업하여 특정 프로세스를 갖는 NodeManager Node들을 실행한다.

#### How YARN works

- 애플리케이션은 Resource Manager(YARN)에게 작업을 클러스터에 분산시키도록 요청한다.

-  YARN은 HDFS의 블록을 특정하여 동일한 노드에 작업을 처리하여 데이터 지역성(Data Locality)를 유지한다.

- 다음과 같은 일정 관리(Scheduling) 옵션이 있다.
  
  - FIFO - First in, First out
  
  - Capacity - YARN 클러스터에서 여러 애플리케이션을 동시에 실행할때, 여유 용량이 충분하다면 병렬적으로 실행한다
  
  - Fair - 클러스터의 리소스를 모두 사용중인 규모가 큰 작업이 실행 중일때, 작은 작업을 실행시키기 위해 큰 규모 작업의 리소스를 가져와 사용한다.

- 

### TEZ

- 방향성 비순환 그래프를 관리한다.

- 얀 위에서 작동한다.

- 내부적으로 매끄럽게 작동하도록 돕는다.

- 기존의 맵리듀스보다 일관성있게 빠르게 작동한다. 

### MESOS

- 얀의 기능을 대신할 수 있다.

- 단일 스케줄러인 얀에 비해, "이중 단계 시스템"을 갖는다.

### ZOOKEEPER

- HBASE와 같은 분선 데이터베이스를 사용중일때, 두개의 다른 마스터 노드를 사용하여 두개 다 응답하게 되면 데이터베이스에 일관성이 사라지게 된다.

- 분산 시스템의 상태를 일정하게 유지하기 위해 개발된 시스템

- 고강용성 맵리듀스, HBASE에 필수적이다.

#### 해결가능한 Failuer modes

- 주키퍼는 현재의 마스터노드를 찾아내고, 해당 마스터 노드가 다운시 다른 백업 마스터 노드를 선별하여 새마스터로 선정하고 추적한다.

- 마스터 노드 하위의 작업자 노드가 다운시에도 애플리케이션이 해당 사실을 전달하고 진행 작업을 다시 적절하게 분산한다.

- 네트워크상에 어떠한 이유로 소통 불가능할 때 해당 상태를 인지하고 일정하지 않은 보고를 작업자를 찾아내고 애플리케이션에게 해결하라고 지시한다.

#### 분산시스템 내의 원시적(Primitive) 실행

- 마스터 선출(Master election) : 어떤 노드가 마스터로  선출된 경우 해당 노드를 데이터에 lock하고, 다른 노드는 lock이 해제 전까지 마스터로 선출되지 않는다.

- 충돌 탐지(Crash detection) : 노드의 연결이 끊어지면 단기성 데이터를 가짐으로 노드의 가용성 확인

- 그룹 관리 : 풀에 어떤 작업자가 가용한지 추적

- 메타데이터 : 데이터베이스의 일관성 유지를 위한 메타데이터 유지

- 주키퍼에서는 APi를 통해 위 4개의 실행을 대신한다.

#### ZooKeeper quorums

- 주키퍼 정족수 : 주키퍼의 클라이언트로서 응답을 받을 때 다른 주키퍼 서버가 해당 응답에 대해 동의해야하는 숫자.

- 주키퍼는 다수의 주키퍼 서버로 구성된 주키퍼 앙상블(ZooKeeper ensemble)로 구성된다.

- 예를 들어, 5개의 서버로 구성된 앙상블에서 정족수를 2개로 설정시 2개의 서버가 네트워크 오류로 다른 서버와 통신할 수 없고 데이터베이스의 일관성이 오염됐을때, 클라이언트는 주키퍼 서버마다 서로 다른 답을 받을 수 있다.

- 위와 같은 경우를 방지하기 위해 주키퍼는 최소 5개의 서버로 구성된 앙상블에 정족수를 3개로 설정한다.

- 정족수는 주키퍼 앙상블의 서버의 대부분을 차지 하도록 설정해야 한다. 이를 통해 더 좋은 실패 회복성을 갖게 된다.

### Oozie

- 하둡 작업을 조직한다.하둡 클러스터의 추가 작업 조직

- 여러개의 작업(sqoop, pig 등)을 추합하여 하나의 워크플로우로 조직한다.

##### 워크플로우 조직하기

- HDFS에 작업 디렉토리 들을 생성한다

- xml 파일로 워크플로우를 작성

- jop.properties에 워크플로우들을 작성한다.

### Zeppelin

- Spark와 강하게 결합되어 있다.

- 데이터와 스크립트를 상호작용한다.

- 제플린 ui에서 필요한 분석에 대한 스크립트를 작성하면 즉각적인 결과확인이 가능하다.
