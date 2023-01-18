[TOC]

# Spark-with-Python 09

## Spark 스트리밍, 구조적 스트리밍 및 GraphX

### Spark 스트리밍

- 연속적인 스트리밍 데이터를 분석할때 사용한다.

- 일정 간격으로 흘러오는 데이터를 수집하여 전송한다.

- 스파크 스트리밍에는 2가지 방법이 있다.
  
  - `Dstream`으로 객체를 분할하여 dictinct한 `RDD`로 나눈다.
    
    - 예를 들면 1초단위로 스트리밍 데이터를 쪼갠다. 
    
    - `RDD`에는 1초 분량의 데이터가 있어 원하는 처리를 진행한다.
  
  - 그리고 `structed streaming`

#### Structed Streaming

- 끊임없이 수신되는 스트리밍 데이터를 데이터 프레임의 형식으로 저장한다.

- 구조화된 데이터 프레임에 스트리밍 데이터가 저장되는데, 단순히 행을 추가함으로 데이터를 저장할 수 있다.

- `RDD`가 사장되는 추세라 데이터프레임 사용을 적극 추천하는듯.
  
  - 다른 `Spark` API 뿐만 아니라 여러 라이브러리에서도 데이터프레임을 사용한다..

### [활동] Python의 구조적 스트리밍

- 실제 로그 기록 데이터를 통해 `Spark Streaming`을 구동해보자.
  
  - 로그 기록을 보니.. 많이든 처리하나보다..

- 계에에에에속 안되다가 뭐가 문제지..뭔가 문제지..
  
  - `hadoop.dll`이라는 파일을 `c:\windows\system32\`에 넣어주니 해결됐다..
  
  - `py4j.protocol.py4jjavaerror: an error occurred while calling o27.text.`이런 오류였다..

---

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
