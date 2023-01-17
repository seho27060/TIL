[TOC]

# Spark-with-Python 06

## 클러스터에서 Spark 실행 - 01

### Amazon Elastic MapReduce 소개

- AWS에서 제공하는 클라우드 클러스터 서비스
  
  - 이름은 MapReduce지만 스파크가 설치되어 있다.

- 따로 클러스터를 구성할 필요없이 YARN, 클러스터 매니저 등 모든 설정이 구성되어 있다.

- 물론 사용한 만큼 비용을 지불하지만..m3.xlarge 인스턴스를 사용하므로 예상치못한 비용 지출에 더욱 주의하자.
  
  - m3.xlarge 인스턴스 10개로 클러스터를 구성하면..1개당 1시간마다 0.26\$고.. 10개면 3.6\$..10시간이면 36\$...

### [활동] AWS/ Elastic MapReduce 계정 설정 및 PuTTY 설정

- AWS의 Elastic MapReduce로 클러스터를 실행시키고, 해당 클러스터를 로컬에 연결해보자.

- EMR로 클러스터를 생성하기 전 key-pair에서 새로운 `.pem`파일을 생성하고 PuTTY를 통해 `.ppk`파일을 생성한다.

### 파티셔닝

- 대용량 데이터를 처리할 때 어떻게 해야 효율적일까?
  
  - 데이터를 분할하여 처리할 수 없을까?

#### Optimizing for running on a cluster:Partitioning

- Spark is not totally MAGIC! - 스파크 하나로는 모든 걸 해결할 수 없다.. 데이터를 어떻게 나눠(partitioned) 처리할 건지 고민해야한다.

- `.partitionBy()`는 RDD의 메서드로 큰 규모의 작업(a large operation)을 partitioning하여 클러스터 관리자가 문제없이 작업을 다루게 한다.
  
  - `.join()`, `cogroup()`, `groupWith()`... 등등 많이 있다.
  
  - 큰 작업을 수행할 시 보통 파티셔닝으로 분할 후 진행한다.

#### Choosing a partition size

- 너무 작은 파티셔닝은 클러스터의 이점을 취할 수 없다.

- 또 너무 많은 파티셔닝은 shuffling data 과정에서 오버헤드를 일으킨다.

- 클러스터의 코어 수 또는 가용 메모리에 최대한 넣을 수 있어야 한다.
  
  - 보통 100개로 파티셔닝을 시작한다. 이후 차차 조정해야함.

--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
