- [udemy HDFS_03](#udemy-hdfs_03)
  - [Spark](#spark)
    - [Spark RDD](#spark-rdd)
      - [Transforming RDD's](#transforming-rdds)
      - [RDD actions](#rdd-actions)
      - [Lazy evaluation](#lazy-evaluation)
  - [Hive](#hive)
    - [Schema On Read](#schema-on-read)
    - [Partitioning](#partitioning)
    - [MySQL과 Hadoop 통합하기](#mysql과-hadoop-통합하기)
      - [Sqoop](#sqoop)
        - [Incremental import, 증분적 불러오기](#incremental-import-증분적-불러오기)

# udemy HDFS_03

## Spark

- 대규모 데이터 처리에 사용되는 신속하고 보편적인 엔진

- 실제 프로그래밍 언어로 스크립트를 작성.

- 복잡한 데이터를 조작, 분석 집계

- 메모리 기반 솔루션, 디스크가 아닌 메모리 내에서 작동

- MapRuduce보다 10배 빠름

- 방향성 비사이클 그래프

- RDD(Resilient Distributed Dataset)

- Components of spark
  
  - Spark Streaming
  
  - Spark SQL
  
  - MLLib
  
  - GraphX

### Spark RDD

- 회복, Resilient

- 분산, Distributed

- 데이터셋, Dataset

#### Transforming RDD's

- map

- flatmap

- filter

- distinct

- sample

- union, intersection, substract, cartesian

#### RDD actions

- collect : RDD의 데이터를 파이썬 객체로 반환

- count : 

- countByValue

- take

- top

- reduce

- etc..

#### Lazy evaluation

- action이 호출되기 전엔 드라이버 프로그램안에서는 아무일도 일어나지 않는다.

## Hive

- SQL을 mapping, reducing을 하도록 변환하여 HDFS에 적용한다.

### Schema On Read

- 구조화 되지 않는 데이터를 가져와 읽는 순간에 스키마를 적용한다.

- 메타스토어(metastore)와 같은 스키마데이터(메타데이터)를 가지고 있어 스키마 적용에 사용된다.

### Partitioning

- 데이터를 분리(partitioned)된 하위 디렉토리에 저장한다.

### MySQL과 Hadoop 통합하기

#### Sqoop

- SQL + Hadoop

-  대용량 데이터 세트를 가져오거나 내보내고 관리

- 가져오거나 내보내는 mapper만 사용

- 대용량 데이터 세트를 위한 기술이니 작은 데이터는 효율이 떨어짐

##### Incremental import, 증분적 불러오기

- 
