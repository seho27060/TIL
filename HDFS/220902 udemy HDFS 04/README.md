# udemy HDFS 04

## Hbase

- HDFS위에 구축된 확장 가능한(Scaleable) 비관계형(Non-relational) 데이터 베이스
- 다른 NoSQL과 같이 쿼리를 갖지 않지만, 특정 질문에 대한 답을 제공하는 API를 갖는다.
- 구글의 BigTable을 그대로 옮겨 구현한것.

### 구조

- HDFS 위에 여러개의 Resion Server로 구성되어 있다.

- 데이터를 HDFS에 입력시, HBase가 자동으로 분리(Auto-shardiung)하여 여러개의 Resion server에 저장한다.

### HBase data model

- 행을 key로 사용한다.

- column familes : 여러개의 컬럼 집합을 열로 저장한다.

- cell : 저장된 컬럼 패밀리을 버전에 따라 조회할 수 있다. 타임스탬프가 자동으로 저장된다.

- Sparse data?

### HBase 접근 방법

- HBase shell

- Java API

- Spark, Hive, Pig

- REST Service, Thrift service, Avro service

## Cassandra

- 마스터노드가 없고, 단일 실패 지점이 없다. 

- 비관계형 데이터베이스, 이지만 제한적인 CQL 쿼리를 사용하낟.

- BigTable, HBase와 비슷한 데이터 모델

- NoSQL with a twist

### 언제 사용해야 하는가

#### CAP

- 일관성(Consistency) : 데이터베이스에 쿼리를 날리면 무슨일이 있어도 응답을 받는다. == 카산드라의 eventually consistent와 매칭됨
- 가용성(Availability) : 항상 작동하여 신뢰할 수 있고, 많은 예비 데이터를 가짐
- 파티션 저항성(Partition tolerance) : 데이터가 쉽게 나눠지고 클러스터에 분산될 수 있음.
- 셋 중 2개만 가질수있다고 한다.
  - HDFS에서는 파티션 저항성을 포기못한다. 
  - 일관성은 Cassandra의 eventually consistent와 대응되므로, 일관성을 포기하고 가용성을 가져간다.

### CQL

- Cassandra's API

- SQL과 비슷하지만 많은 제한이 있다.
  
  - JOIN불가, 비관계형데이터이므로
  
  - 모든 쿼리는 primery key를 사용해야 한다.

- 
