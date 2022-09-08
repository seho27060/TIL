[TOC]

# udemy HDFS_07

- 실시간 데이터를 스트리밍하고, 데이터 수신 즉시 분석하여 결과 출력하기.

## Spark Streaming

- 데이터 스트림 발생

- Flume, Kafka, 연결 소켓을 통해 데이터 수신/ 클러스터에 분산된 수신기 생성

#### DStreams(Discretized Streams)

- #### Windowing

- Batch interval : 얼마나 자주 데이터를 샘플링, 처리하는가

- Slide interval : 얼마나 자주 윈도 변환을 계산하는가

- Window interval : 윈도 간견은 윈도 변환을 위해 얼마나 시간을 되돌리는가

- 1초의 배치 간격, 3초의 윈도 간격, 2초의 슬라이드 간격 
  
  - 매초 마다 배치 정보가 RDD에 생성
  
  - 2초마다 슬라이드 간격이 결과 계산
  
  - 3초마다 윈도에서 얼마나 시간을 되돌릴지 결정### 

#### detail-index1

## Storm

- 스파크 스트리밍과 다르게 이벤트 별로 데이터 수신

- 
