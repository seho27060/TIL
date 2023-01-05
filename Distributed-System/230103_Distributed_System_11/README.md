- [Distributed System 11](#distributed-system-11)
  - [분산형 MongoDB](#분산형-mongodb)
    - [MongoDB](#mongodb)
      - [Document Oriented DB(문서 지향 DB)](#document-oriented-db문서-지향-db)
      - [MongoDB CRUD Operations](#mongodb-crud-operations)
      - [로컬에서 MongoDB 인스턴스 실행](#로컬에서-mongodb-인스턴스-실행)
    - [데이터 복제를 이용한 MongoDB 확장](#데이터-복제를-이용한-mongodb-확장)
      - [MongoDB - Replica Sets](#mongodb---replica-sets)
      - [MongoDB - Write Concern](#mongodb---write-concern)
      - [MongoDB - Read Preference](#mongodb---read-preference)
    - [데이터 샤딩을 이용한 MongoDB 확장](#데이터-샤딩을-이용한-mongodb-확장)
      - [MongoDB Sharding Strategies](#mongodb-sharding-strategies)
      - [MongoDB Sharded Cluster](#mongodb-sharded-cluster)
      - [Note](#note)


# Distributed System 11

## 분산형 MongoDB

### MongoDB

- 확장가능한(Scalable) NoSQL 데이터베이스

- 아주 심플한 데이터 모델을 갖음

#### Document Oriented DB(문서 지향 DB)

- 테이블에 데이터를 저장하는 대신 데이터베이스에 직접 객체를 만든다.

- JSON을 BSON으로 내부적으로 변환하여 객체로 저장한다.

- SQL DB vs MongoDB Terminology
  
  | SQL         | MongoDB    |
  | ----------- | ---------- |
  | Table       | Collection |
  | row         | object     |
  | column      | field      |
  | Primary key | Object ID  |

#### MongoDB CRUD Operations

- 도큐먼트의 '\_id'를 제외하고 CRUD를 작업할 수 있다.

- Create
  
  - `db.collection.inserOne(object)`
  
  - `db.collection.inserMany([object1, object2,...])`

- Read
  
  - `db.collection.find(filter)`

- Update
  
  - `db.collection.updateOne(filter,update action)`
  
  - `db.collection.updateMany(filter,update action)`
  
  - `db.collection.replaceOne(filter, replacement)`

- Delete
  
  - `db.collection.deleteOne(filter)`
  
  - `db.collection.deleteMany(filter)`

#### 로컬에서 MongoDB 인스턴스 실행

- Mongodb를 OS에 맞게 다운로드

- mongosh를 다운로드하여 몽고디비 쉘 실행

- 몽고쉘상에서 위의 CRUD 커맨드로 디비 작업을 수행할 수 있다.

- 커맨드에 사용되는 `filter`의 경우 몽고디비에서 제시하는 키워드를 사용하면 원하는 조건의 데이터를 읽을 수 있다.

### 데이터 복제를 이용한 MongoDB 확장

#### MongoDB - Replica Sets

- 데이터 가용의 중복성과 개별 노드에 장애 발생 시 복원성을 제공하기 위해 여러 mongodb 인스턴스를 실행하여 데이터를 복제한다.

- mongdb 인스턴스 그룹은 같은 데이터를 갖고 있고 이를 복제 세트(Replica Set)라고 한다.

- 복제 세트 구조 
  
  - 복제 세트에는 주 노드(Primary node)가 하나 있고 읽기와 쓰기 작업을 전담한다.
    
    - 이외 나머지 복제 노드는 보조 노드(Secondary node)로 간주한다. 
    
    - 마스터-슬레이브 아키텍쳐의 변형
  
  - 보조 노드는 주 노드와 지속적으로 동기화되어 최신 상태를 유지한다.
  
  - 주 노드가 작동 중지(Shut down)되면 보조 노드들 중 새로운 주 노드를 선출(reelection)한다.
    
    - 주 노드가 선출되기 전까지 모든 쓰기 작업은 중지된다.
    
    - 작중이 중지된 노드는 복구 후 보조 노드로 참여한다.

#### MongoDB - Write Concern

- 기본적으로 쓰기(Wrtie) 작업은 데이터를 성공적으로 읽어서 주 노드에 추가하는 즉시 승인된다.
  
  - 만약 주 노드에 오류가 발생하여 쓰기 작업이 완료되지 않는다면.. 데이터 손실이 발생한다.

- 예상치 못한 오류로 데이터 손실을 방지하기 위해 쓰기 작업 중 writeConcern을 지정할 수 있다.
  
  - 데이터 추가 커맨드에 `majority`를 옵션으로 추가하여 쓰기 작업을 진행시, 클러스터의 크기와 관계없이 쓰기 작업을 과반수의 노드에 복제할 수 있다.

#### MongoDB - Read Preference

- 모든 읽기 작업 또한 엄격한 일관성을 보장하기 위해 주 노드에서 직접 처리한다.
  
  - 읽기 작업 커맨드에 `readPref({"primaryPreferred"})`를 추가하여 주 노드가 가용상태(available)라면 주 노드에서 작업을 수행하고, 
  
  - 그렇지 않아 주 노드가 선출되지 않을 경우 동기화가 심하게 어긋나지는 않은 보조 노드에서 작업을 수행한다.

- 읽기 작업이 주 노드에 너무 몰려있고, 일관성 요구 조건이 최종 일관성(eventually consistency)로 만족한다면 `readPref({"secondary"})`로 설정할 수 있다.

- 여러 물리적 위치에 복제 세트가 위치한 경우 `readPref({"nearest"})`로 어플리케이션 대기시간이 가장 짧은 노드에서 작업을 수행할 수 있다. 
  
  - 오래된 데이터를 읽어올 수 있지만 빠른 응답이 필요한 경우 사용한다.

### 데이터 샤딩을 이용한 MongoDB 확장

#### MongoDB Sharding Strategies

- 샤딩을 위해 샤딩 키를 선정해야하며 이는 어느 값이든 가능하다.
  
  - 다만 이후 수정이 불가하기 때문에
  
  - 컬렉션의 증가에 따른 확장성을 보장해야하고
  
  - 요청 쿼리의 증가에 따른 효율적인 쿼리를 보장해야 한다.

- 데이터(도큐멘트)는 샤딩 키(Sharding key)에 해쉬 함수(Hash Function)을 적용하여 작은 단위(Chunk)로 나눈다.
  
  - **Range Routing** - 키값을 정해진 범위에 따라 할당될 청크를 결정한다.
  
  - **Hash Functoin**

- 도큐멘트들이 할당된 여러 청크는 여러 샤드(Shard)에 균등하게 분배되어 저장된다.
  
  - 데이터베이스의 규모가 커짐에 따라 청크의 크기도 커지는데 일정 범위(Threshold)를 넘으면 다시 작은 청크로 분할하여 부하를 분담한다.

#### MongoDB Sharded Cluster

- 클라이언트 어플리케이션이 쿼리를 날릴때 어떤 샤드들의 조합으로 작업을 해야하는지 알기 위해 라우터(Router,mongos라는 인스턴스로 실행)라는 요소가 필요하다

- 라우터는 쿼리를 해석하여 필요한 청크가 있는 주소에 작업을 실행한다.

- 이때 청크의 주소는 설정 서버(Config Server, mongod 인스턴스)가 가지고 있어 라우터에게 정보를 알려준다.
  
  - 설정 서버의 정보는 중요하므로 복제 세트로 운영한다.

- 내결함성을 위해 샤드들은 각각의 복제 세트로 운영한다.

- 라우터 또한 여러 인스턴스로 실행한다.

- 이를 통해 **단일 장애점이 없음**을 보장할 수 있다.

#### Note

- 샤딩을 통해 고가용성과 내결함성을 갖는 디비로 커스터마이징이 가능하다..

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
