[TOC]

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

#### detail-index1
