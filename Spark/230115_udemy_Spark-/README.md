[TOC]

# Spark-with-Python 05

## Spark 프로그램의 고급 예제 02

### 슈퍼히어로의 Degrees of Separation: 어큐뮬레이터 및 Spark에서 BFS 구현

- Degrees of Separation - 분리 정도, 그래프 상에서 A노드에서 B노드까지 거쳐야하는 간선의 개수

- ```textile
  1234 2324 3435 34546 
  45635 352 3543 213 523 353 1 2 3434
  ```
  
  위와 같은 데이터가 있을때, 가장 첫번째 히어로id와 그 위에 이어지는 id들이 연결되었다는 뜻이다.
  
  이때 어떻게 **BFS**를 **Spark**내에서 구현할 수 있을까?

- ```textile
  (45635, (352, 3543, 213, 523, 353, 1, 2, 3434, 9999) and white
  ```
  
  위와 같이 변환한다. (현재 노드,(연결된 노드들...), 닿는데 거리,지나갔는지 여부)

- 변환된 데이터를 mapper와 Reducer로 생성

- **Accumulator** : 클러스터내에 공유된(broadcast) 자원을 증가할 수 있게함. 모든 노드를 동시에 유지 및 관리하는  카운터
  
  ```python
  hitCounter = sc.accumulator(0)
  ```
  
  위와 같이 `Spark Context`를 통해 `accumulator` 객체를 할당한다.
  수퍼히어로를 BFS로 찾기 예제와 같은 경우, 원하는 히어로를 찾았을 경우 `hitCounter`의 값을 증가시켜, 모든 노드들이 작업이 완료됐음을 알 수 있다. 

### Spark cache() 및 persist()의 항목 기반 협업 필터링

- 항목 기반 협업 필터링(Item-based Collaborative Filtering) : 유저의 item 기록과 가장 매칭되는(유사성있는) 다른 유저의 item 기록을 토대로 새로운 아이템을 추천해준다.

#### Caching Datasets

- 스파크 SQL로 쿼리를 날리는데 있어서, 여러번 동일한 데이터프레임에 동일한 쿼리를 날릴때 Caching하는게 좋다.
  
  - 그렇지 않으면 `Spark`는 전체 데이터프레임에 대해 재평가(re-evaluation)을 하게 되고 이는 오버헤드로 이어진다.

- `.cache()`나 `.persist()`로 캐싱한다.
  
  - 위 두개 메서드의 차이는 `.cache()`는 메모리상에 캐싱을 하고
  
  - `.persist()`는 메모리가 아닌 디스크에 캐싱한다. 디스크에 캐싱함으로 노드의 실패나 복구에 대응이 가능하다.

> BFS나 아이템 기반 협업 필터링이나.. 간단한 알고리즘이라고 할 수 있다. 이때 문제는 어떻게 Spark 내에서 구현할 것인가?, 어떤 방식이 분산 시스템의 이점을 활용할 수 있는 방법인가?, 어떻게 클러스터에 존재하는 모든 노드에서 작동시킬 것인가?..와 같이 있다. 이러한 문제를 본 강의에서는 **Spark Problem(스파크 문제)** 라고 한다.

### [활동] Spark의 클러스터 관리자를 사용하여 유사한 영화 스크립트 실행

- ```python
  spark = SparkSession.builder.appName("MovieSimilarities").master("local[*]").getOrCreate()
  ```
  
  해당 작업을 위해 `.master("local[*]")`을 설정한다. 이는 해당 마스터 머신의 모든 CPU 자원을 사용한다는 옵션이다.
  
  - 실제 클러스터 작동에서..많이 사용하진 않을거다. CPU를 모두 사용하면 클러스터 내 다른 노드가 작동을 못하니까.

- 사용할 데이터를 위해 스키마를 설정하고..text파일이므로 charset 설정하고..
  
  불러온 데이터에서 사용하지 않는 데이터(컬럼, 행)을 줄여 카디널리티를 축소한다.
  
  ```python
  ratings = movies.select("userId", "movieId", "rating")
  ```

- self-join으로 1개 데이터로 다른 아이템끼리의 쌍을 만들고..코사인 유사도를 계산하고..

--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
