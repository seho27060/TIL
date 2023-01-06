[TOC]

# Spark-with-Python 01

## Spark 기본 사항 및 RDD 인터페이스

### Spark 3의 새로운 기능

- 빨라짐

- GPU 인스턴스 지원

- 더 좋은 쿠버네티스 지원

- 이진 파일 지원

- SparkGrapher

### Spark 소개

> 큰 규모의 데이터 처리를 위한 빠른 일반 엔진
> 
> A fast and general engine for large-scale data processing

#### IT'S SCALABLE

- 스파크 구성
  
  - Driver Program - Spark Context
    
    - Cluster Manager(Spark, YARN)
      
      - Executor - Cache -Tasks
      
      - Executor - Cache -Tasks
      
      - Executor - Cache -Tasks
      
      - ...

- 컴퓨터의 전체 클러스터의 규모를 측정하여 수평 분할(Scale out)하고 수평적인 확장성을 갖는다.
  
  - 가장 이상적으로 CP 코어 하나마다 Executor를 할당

- 사용자와 개발자의 관점에서는 하나의 프로그램으로 작동하는 거처럼 보임

#### IT'S FAST

- 하둡 MapReduce보다 Spark가 약 10배가량 빠름

- **DAG(directed acyclic graph, 비순환 그래프)** 엔진을 사용한 성과 산출

#### IT'S HOT

- 많은 기업에서 이미 스파크를 사용하고 있다.

#### IT'S NOT THAT HARD

- 파이썬, 자바, 스칼라로 코딩 가능

- **RDD(Resilient Distributed Dataset, 탄력적 분배 데이터세트)** 라는 단 한 가지 개념으로 구축되었음

#### COMPONENTS OF SPARK

- **SPARK CORE**
  
  - SPARK Streaming - 웹 로그 셋 분석
  
  - Spark SQL - HIVE 컨텍스트에서 스파크를 작동하도록 하고, 구조화된 데이터를 처리하게 함.
  
  - MLlib - 머신 러닝 알고리즘 장치 시리즈. 머신 러닝이나 데이터 마이닝, 통계 기법 사용 가능
  
  - GraphX

### The Resilient Distributed Dataset

#### RDD

- 스파크의 핵심은 '복구 가능한 분산 데이터 세트'

- 스파크, 스파크 SQL, MLlib 에서 사용하는 객체

- RDD 객체를 생성 후, 데이터에 데이터 처리를 분산하여 할당

- 분산(Distributed)와 변형(Resilient)를 통해 가용성과 내결함성을 가짐
  
  - 스파크나 클러스터 매니저에 의해 수행된다.

#### Spark Context

- Driver Program에 의해 생성됨

- 스크립트 상에서 `sc`로 사용됨

- RDD에 변형하고 분산하는 작업을 담당하며 RDD를 생성한다.

- `JDBC`, `Cassandra`, `HBase`, `Elasticsearch`, `JSON`,`CSV` 등 여러 데이터베이스와 데이터포맷에 인터페이스가 있어, 해당 매체로도 RDD를 생성(Creating) 가능하다.

- `map`, `flatmap`,`filter`,`distinct`, `sample`, `union`, `intersection`, `subtract`, `cartesian` 등의 함수로 RDD를 변환(Transforming)한다.

#### RDD ACTIONS

- `collect`, `count`, `countByValue`, `take`, `top`, `reduce` 등등 여러 함수로 RDD에 작업을 수행한다.
  
  - `collect`로 원하는 값만 출력하거나
  
  - `countByValue` 원하는 값을 세거나
  
  - `reduce`로 모든 값에 특정한 연산을 하여 하나의 RDD로 합쳐주거나
  
  - 등등 여러 작업을 수행 가능하다~~~~

#### LAZY EVALUATION

- 스파크가 빠른 이유는 액션이 입력되면 바로 유향 비순환 그래프를 형성하기 때문
  
  - 우리가 어떤 값을 원하는지, 해당 값을 위해 어떤 작업을 해야하는지 최적화된 방법을 계산함

- 스파크 드라이버 스크립트 내에서 RDD에 **액션을 실행하기 전**까지 **아무런 일도 일어나지 않는다.**

### 등급 히스토그램 워크스루

- 전 강의에서 실습해본 히스토그램 출력의 워크스루(work through)를 확인해보자.

- 필요 모듈 import 
  
  ```python
  from pyspark import SparkConf, SparkContext
  import collections
  ```
  
  `SparkConf` - `SparkContext` 설정/ `SparkContext` - RDD 관련 코딩의 시작점

- SparkContext 설정과 생성
  
  ```python
  conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
  sc = SparkContext(conf = conf)
  ```
  
  `conf`에 local을 마스터 노드로 설정하고 해당 설정 객체 `conf`를 `SparkContext`에 할당하여 `sc` 객체를 생성했다.

- 파일을 RDD 객체로 불러오기
  
  ```python
  lines = sc.textFile("파일경로)
  ```
  
  텍스트 파일을 읽어오고 한 줄이 하나의 RDD의 값이 된다.(5줄이라면 5개의 RDD로 변환)

- RDD에서 데이터 추출하기
  
  ```python
  ratings = lines.map(lambda x :x.split()[2])
  ```
  
  `lambda`를 활용하여 함수형 프로그래밍으로 데이터 추출

- RDD에 액션 넣기
  
  ```python
  result = ratings.coutByValue()
  ```
  
  RDD를 원하는 형태로 변환한다.

- Sort 와 Display
  
  ```python
  sortedResults = collections.OrderedDict(sorted(result.items()))
  for key, value in sortedResults.iteritems();
      print "%s %i" % (key, value)
  ```
  
  뭐 자주 쓰던 파이썬의 코드와 상당히 비슷하다.

### 키/ 값 RDD 및 연령별 평균 친구 예시

- RDD의 장점은 key-value형식의 데이터를 구조화 할 수 있다는 점.

#### Spark can do special stuff with key/value data

- `reduceByKey()` : 우리가 정의한 함수를 이용하여 같은 key값의 field 값을 활용하는 함수
  
  - 특정 나이대는 몇명의 친구를 갖고 있는가?

- `groupByKey()` : 같은 key를 갖는 값 끼리 그룹화함

- `sortByKey` : 같은 key끼리 분류

- `join`, `rightOuterJoin` 등등 SQL에서 사용하는 것과 같은 함수도 있다.

#### Mapping just the values of a key/value RDD

- key/value 데이터에 대하여 변형된 RDD에 있는 키를 수정하지 않을 때는 `map`,`flatMap` 대신 `mapValues()`, `flatMapValues()`를 사용한다.
  
  - key/value RDD의 **핵심**적인 부분

- 데이터를 셔플하는 대신 기존 RDD에서 분할된 데이터를 그대로 유지하여 더 효율적이다.

--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
