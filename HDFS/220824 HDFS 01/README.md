- [HDFS_01](#hdfs_01)
  - [개요](#개요)
    - [병렬분산 알고리즘](#병렬분산-알고리즘)
      - [MapReduce Framework](#mapreduce-framework)
      - [MapReduce Programming Model](#mapreduce-programming-model)
      - [특징](#특징)
      - [MapReduce Phase](#mapreduce-phase)
  - [Hadoop](#hadoop)
      - [MapReduce 의 함수](#mapreduce-의-함수)
      - [MapReduce를 통한 WordCounting 알고리즘](#mapreduce를-통한-wordcounting-알고리즘)
    - [Overview of MapReduce](#overview-of-mapreduce)

# HDFS_01

## 개요

- 자바를 기반으로 하둡을 이용해보자.

### 병렬분산 알고리즘

- scale-out: 아주 많은 값 싼 서버를 이용/ scale-up : 적은 수의 비싼 서버 이용

- 데이터중심 프로세싱(Data-intensive processing)에서는 scale-out를 사용해야 이점이 있다.

- 한대가 아닌 여러대의 컴퓨터의 능력이 데이터 처리에 용이하기 때문이다.

- **맵리듀스(MapReduce)** 프레임워크가 하는 일.

#### MapReduce Framework

- 비용이 적은 컴퓨터들을 모아 클러스터를 만들고, 빅에티러르 처리하기 위한 스케일러블(scalabe: 부하또는 데이터 가 급증해도 프로그램이 멈추거나 성능이 떨어지지 않음) 병렬 소프트웨어의 구현을 쉽게 도와주는 프로그래밍 모델

- 맵리듀스의 우수한 구현으로 오픈소스 **하둡(Hadoop)** 이 있다.

#### MapReduce Programming Model

- 함수형 프로그래밍 언어의 형태

- 유저는 아래 3가지 함수를 구현하여 제공해야한다
  
  1. Main  함수
  
  2. Map 함수 : (key1, val1) -> [(key2,val2]
  
  3. Reduce : (key2,[val2]) -> [(key3, val3)]

#### 특징

- 맵리듀스 프레임워크에서는 각각의 레코드 또는 튜플은 키-밸류 쌍으로 표현된다.

- 메인 함수를 한개의 마스터머신에서 수행한다. 머신은 맵 함수를 수행전 전처리를 하거나, 리듀스 함수의 결과를 후처리하는데 사용한다.

- 컴퓨팅은 맵과 리듀스 라는 유저 정의 함수 한 쌍으로 이뤄진 맵리듀스 페이즈를 한번 수행하거나 여러번 반복 수행할 수 있다.

- 한번의 **맵리듀스 페이즈**는 맵 -> 리듀스 함수 호출로 이뤄지는데, 맵 함수 이후 컴바인(combine) 함수를 중간에 수행할 수 있다.

#### MapReduce Phase

1. Map Phase
   
   - 제일 먼저 수행된다. 데이터의 여러 파티션(partition)에 병렬 분산으로 호출되어 수행
   
   - 각 머신마다 수행된 Mapper는 맵 함수가 입력데이터의 한 줄마다 맵 함수를 호출
   
   - Map 함수는 (Key,value) 쌍으로 입력을 받고, 같은 형태로 결과를 출력한다.
   
   - 한줄 한줄 Map 함수가 실행되는거처럼 보이지만, 실제론 여러대의 컴퓨터가 병렬적으로 처리한다.

2. Shuffling Phase
   
   - 모든 머신에서 맵 페이즈가 끝나면 실행
   
   - 맵 페이즈에서 각각의 머신으로 보내진 키-밸류 쌍에서 키값을 이요하여 정렬한후, 각각의 키 마다 **같은 키를 가진 키-밸류 쌍**을 모아 value-list 로 만든다음 key-value-list 형태로 key에 따라 여러 머신에 분산해서 보낸다.

3. Reduce 페이즈
   
   - 모든 머신에서 셔플링 페이즈가 끝나면 실행
   
   - 셔플링 페이즈에서 해당 머신으로 보내진 각각의 (key,value-list) 쌍마다 리듀스 함수가 호출되어 할당된 작업을 실행하고 반환한다.

## Hadoop

- Apache 프로젝트의 맵리듀스 프레임워크 오픈소스

- 하둡 분산 파일 시스템(Hadoop Distributed File System - HDFS)
  
  - 빅데이터 파일을 여러대의 컴퓨터에 나누어 저장한다.
  
  - 각 파일은 여러 개의 순차적 블록으로 저장
  
  - 하나의 파일의 각각의 블록은 fault tolerance(시스템 구성 부품의 일부에서 결함 또는 고장이 발생해도 정상적으로 기능을 수행하는 것) 를 위해 여러개로 복사되어 여러 머신에 저장된다.

- 주요 구성 요소
  
  - MapReduce - 소프트웨어의 수행 분산
  
  - Hadoop Distrubuted File System - 데이터를 분산

- 한 개의 NameNode(master)와 여러개의 Datanode(slaves)
  
  - Namenode : 파일 시스템을 관리, 클라이언트가 파일에 접근하도록 함
  
  - Datanode : 컴퓨터에 들어있는 데이터를 접근할 수 있게 함.

#### MapReduce 의 함수

- 맵 함수
  
  - `Mapper`클래스를 상속받아 맵 메서드를 수정
  
  - 입력 텍스트 파일에서 라인 단위로 호출된다. 입력은 키-밸류(key, value-list) 형태

- 리듀스 함수
  
  - `Reducer`클래스를 상속받아서 리듀스 메서드를 수정
  
  - 셔플링 페이즈의 출력(키-밸류(key,value-list))를 입력으로 받는다.
  
  - value-list는 맵함수의 출력의 key를 갖는 (key,value) 쌍들의 value들의 리스트

- 컴바인 함수
  
  - 리듀스 함수와 유사한 함수, 각 머신에서 맵페이즈에서 맵 함수의 출력 크기를 줄여 셔플리 페이즈와 리듀스 페이즈의 비용을 줄여주는 역할을 한다.

#### MapReduce를 통한 WordCounting 알고리즘

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-01-19-08-image.png)

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-01-19-53-image.png)

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-01-20-12-image.png)

- Combine 함수 
  
  - Map 함수의 결과 크기를 줄여줌
  
  - 맵리듀스 알고리즘을 최적화할 수 있음

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-01-24-42-image.png)

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-01-26-47-image.png)

### Overview of MapReduce

- Mapper and Reducer 
  
  - 각 머신에서 독립적으로 수행

- Combine functions
  
  - Map - Comebine - Reduce 순서로 실행, 리듀스가 하는 일을 부분적으로 수행
  
  - 셔플링 비용과 네트워크 트래픽 감소

- Mapper와 Reducer가 필요하다면 setup() and cleanup() 수행
