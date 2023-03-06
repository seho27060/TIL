- [Spark-with-Python 04](#spark-with-python-04)
  - [Spark 프로그램의 고급 예제](#spark-프로그램의-고급-예제)
    - [\[활동\] Hive를 사용하여 가장 인기 있는 영화 찾기](#활동-hive를-사용하여-가장-인기-있는-영화-찾기)
    - [\[활동\] 브로드캐스트 변수를 사용하여 ID번호 대신 영화 이름 표시](#활동-브로드캐스트-변수를-사용하여-id번호-대신-영화-이름-표시)
      - [Introducing Broadcast Variables](#introducing-broadcast-variables)
      - [예시 코드](#예시-코드)
    - [\[활동\] 소셜 그래프에서 가장 인기 있는 슈퍼히어로 찾기](#활동-소셜-그래프에서-가장-인기-있는-슈퍼히어로-찾기)

---

# Spark-with-Python 04

## Spark 프로그램의 고급 예제

### [활동] Hive를 사용하여 가장 인기 있는 영화 찾기

- id, 영화제목, 점수, 타임스탬프 형식의 리뷰 데이터를 활용하여 가장 인기 있는 영화를 찾자

- "인기 있는"의 정의가 뭐지? 
  
  - 평점이 높은 영화?
  
  - 평가가 많은 영화?

- 해당 예제에서는 영화 ID로 group by하여 리뷰를 count함

### [활동] 브로드캐스트 변수를 사용하여 ID번호 대신 영화 이름 표시

- 영화 id와 제목이 있는 u.item file로 Readable하게 출력해보자

#### Introducing Broadcast Variables

- **Broadcast** : 각 Executor에 할당하여 언제나 접근 가능하도록 함.
  
  - Spark Context에 적재하여 언제든지 사용 가능하다.
  
  - 사용할때는 `.value()`를 통해 객체로 받아 사용한다.

- 여러 노드로 구성된 Cluster에 특정 데이터(객체, 사전..whatever)를 broadcast할 경우, 클러스트 내의 각각의 노드에서 사용할 수 있다.
  
  > 스파크는 보통 "분산 시스템"과 같은 클러스터에서 실행되며, 클러스터의 노드들은 공통된 환경의 자원을 사용하는게 아니다. 서로 "분리"되어 있다. broadcast를 통해 모든 노드들이 사용 가능한 공유 자원을 등록할 수 있는 것이다.

#### 예시 코드

- `nameDict`에 `Spark Context` 객체의 `broadcast`로 `loadMovieNames`와 같은 UDF(User Defined Function)의 반환값을 등록한다.
  
  ```python
  spark = SparkSession.builder.appName("PopularMovies").getOrCreate()
  
  nameDict = spark.sparkContext.broadcast(loadMovieNames())
  ```
  
  `nameDict`는 영화 id와 제목이 매핑된 "사전"을 `broadcast` 객체로 갖는다.

- 필요에 의해 생성된 UDF를 `Spark SQL`로 변환하여 사용할 수 있도록 `pyspark.sql.functions`에 `udf`로 등록한다.
  
  ```python
  def lookupName(movieID):
      return nameDict.value[movieID]
  
  lookupNameUDF = func.udf(lookupName)
  ```
  
  이제 UDF를 `Spark SQL`에서 사용할 수 있다.
  
  ```python
  # Add a movieTitle column using our new udf
  moviesWithNames = movieCounts.withColumn("movieTitle", lookupNameUDF(func.col("movieID")))
  ```

- `broadcast`한 "영화제목 사전"과 UDF를 활용하여 아래와 같이 Readable하게 출력하였다.
  
  ![](C:\Users\seho2\AppData\Roaming\marktext\images\2023-01-12-23-28-46-image.png)

### [활동] 소셜 그래프에서 가장 인기 있는 슈퍼히어로 찾기

- 첫번째 id가 뒤에 이어지는 id의 히어로와 관계가 있다는 수퍼히어로 Id가 나열된 "Marvel-graph" 데이터와

- 수퍼히어로 id와 이름이 매칭된 "Marvel-names" 데이터로 인기 있는 히어로를 찾아보자

- schema가 없는 "Marvel-names"를 스키마를 대입하여 불러오고..line으로 구성된 "Marvel-graph"를 불러온다.

- "Marvel-graph" 데이터의 각 line을 가장 첫번째 히어로 id와 그와 연관된 히어로 id들로 구분하여 key = 히어로 id, value = 연관 히어로 id들의 갯수로 구분하여 Dataframe을 생성한다.
  
  ```python
  connections = lines.withColumn("id", func.split(func.col("value"), " ")[0]) \
    .withColumn("connections", func.size(func.split(func.col("value"), " ")) - 1) \
    .groupBy("id").agg(func.sum("connections").alias("connections"))
  ```
  
  "히어로 id" : 연관된 히어로 id 개수 와 같이 구성된다.

- 연관 히어로 id 개수를 기준으로 내림차순 sort후 가장 첫번째(가장 연관이 많은) 히어로 id를 "Marvel-name" 사전을 활용하여 해당하는 히어로 네임을 출력한다.
  
  ```python
  mostPopular = connections.sort(func.col("connections").desc()).first()
  
  mostPopularName = names.filter(func.col("id") == mostPopular[0]).select("name").first()
  
  print(mostPopularName[0] + " is the most popular superhero with " + str(mostPopular[1]) + " co-appearances.")
  ```

- 결과는 아래와 같다.
  
  ![](C:\Users\seho2\AppData\Roaming\marktext\images\2023-01-12-23-50-33-image.png)

--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
