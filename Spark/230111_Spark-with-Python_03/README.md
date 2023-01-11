[TOC]

# Spark-with-Python 03

## SparkSQL, DataFrames 및 DateSets

### SparkSQL 소개

- 아마 스파크에서 가장 중요한 부분

#### Working with structured data

- RDD를 `DataFrame` 객체로 확장
  
  - `SQL`쿼리 사용가능
  
  - 다양한 데이터 포맷(json, hive, parquet 등등)로 읽기/쓰기 가능
  
  - 구조화된(Structured) 데이터로 작업할 수 있다.

#### Using spark SQL in python

- `SparkSession`을 생성하여 가상의 데이터베이스에서 `SQL`을 사용할 수 있다.

- ```python
  from pyspark.sql import SparkSession, Row
  spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
  inputData = spark.read.json(datafile)
  inputData.createOrReplaceTempView("myStructuredStuff")
  myResultDataFrame = spark.sql("SELECT foo FROM bar ORDER BY foobar")
  ```

- `DataFram`객체에 `show`, `select`, `filter`, `groupby`, `rdd().map(function)`와 같은 함수로 여러 기능을 수행할 수 있다.

#### DataFrames are the new HOTNESS

- `RDD`를 적게 쓰고 `DataFrame`을 많이 사용하는 추세이다.

- `MLlib`,`Spark Streaming`과 같은 주요 스파크 API에서 `DataFrame`을 많이 쓴다.

#### DataFrames VS DataSets

- `DataFrames`는 행 객체로 구성된 `DataSet` 객체이다.

- `DataSet`의 경우, 데이터 타입을 명시한다.
  
  - 파이썬은 untyped하다. 그래서 `DataSet`을 많이 사용하지 않는다.

- 최적화와 저장의 효율성 측면에서 `Scala`를 사용한다면 `DataSet`을 사용함으로 많은 이점을 얻을 수 있다.

#### SHELL access

- `Spark SQL`을 통해 `SQL` Shell을 사용할 수 있다.

- `jdbc`나 `odbc`서버에 `Spark SQL`을 노출할 수 있다.

#### User-Defined Functions(UDF's)

- 사용자가 직접 정의한 함수를 적용할 수도 있다.

- 생성한 `spark session`에 직접 정의한 함수를 `udf`에 등록하여 `Spark SQL`에 `SQL` 쿼리로 사용할 수 있다.
  
  ```python
  def square(x):
      return x*x
  
  spark.udf.register("square", square, integerType())
  df = spark.sql("SELECT square('someNumericField') FROM tableName)
  ```

#### [활동] DataFrame에서 SQL 명령어 및 SQL 스타일 함수 실행하기

- 아래와 같이 `SparkContext`로 불러온 데이터 RDD를 캐싱하고 데이터베이스 처럼 사용 가능하도록 `View`로 생성해준다.
  
  ![](https://user-images.githubusercontent.com/81341784/211871671-38e3a8ab-60b1-4f50-a0e5-324eda8c3ae2.png)

- `Spark SQL`을 아래와 같이 사용한 후
  
  ![](https://user-images.githubusercontent.com/81341784/211871722-14c35a89-3165-45cc-a65a-d71233038089.png)
  
  `for`를 통해 출력해보자
  
  ![](https://user-images.githubusercontent.com/81341784/211871754-624e68fa-a0de-4229-8c93-483b3f338f39.png)

- 생성한 `View`에 내장된 함수를 사용하여 다양한 작업을 수행 가능하다.
  
  ![](https://user-images.githubusercontent.com/81341784/211871786-b1b03181-7402-4b30-ba3d-08b930999695.png)
  
  ![](https://user-images.githubusercontent.com/81341784/211871809-310ca080-a936-4aa1-8260-af1f7e67850b.png)

### RDD 대신 DataFrame 사용하기

- `SparkContext`를 통해 RDD로서 데이터를 불러오는게 아닌 `spark.read`로 데이터를 `DataFrame`으로 불러온다.
  
  ![](https://user-images.githubusercontent.com/81341784/211871830-245732ca-439b-4ee3-a6de-46df295f88f3.png)
  
  - `read.option`을 통해 raw데이터의 구조에 따라 원하는 옵션을 줄 수 있다.
  
  - `select`, `filter`,`groupby`와 같은 `DataFrame`의 내장함수로 원하는 값을 출력할 수 있다.
  
  ![](https://user-images.githubusercontent.com/81341784/211871888-20d65f2c-7ad7-42ce-be08-343132faa03f.png)![](https://user-images.githubusercontent.com/81341784/211872014-ee7ca038-7d37-4722-b491-11d77d3a781a.png)
  
  함수에 대한 출력이 아주 상당히 이쁘게 나온다. ㅎ...

### [연습] DataFrame으로 연령별 친구 구하기

- `userID`, `name`, `age`, `friends` 컬럼을 갖는 테이블에서 `age`별 `friends`의 평균을 구해보자.

- ```python
  friendsByAge.groupBy("age").avg("friends").show()
  ```
  
  `SQL`과 비슷하다. `age`로 `groupby`해주고 `friends`에 대한 평균(`avg`)를 산출했다.
  
  ![2023-01-12-01-00-08-image](https://user-images.githubusercontent.com/81341784/211872038-bd7c4dcb-f991-48ca-ae43-beef83591fad.png)

- ```python
  from pyspark.sql import functions as func
  friendsByAge.groupBy("age").agg(func.round(func.avg("friends"), 2)).sort("age").show()
  ```
  
  집계함수 `agg`와 `pyspark.sql`의 내장된 `functions`를 활용하여  여러 함수를 복합적으로 사용 가능하다.
  
  위의 예시에서는 `friends`에 대한 평균을 소수 2번째 자리까지 `round`하여 산출한다.
  
  ![2023-01-12-01-02-01-image](https://user-images.githubusercontent.com/81341784/211872060-14142e81-473f-48a3-88f4-a3d2e36d6909.png)

- `pyspark.sql.functions` : Spark SQL내의 함수를 모아논 모듈. 명시하거나 객체로 사용 가능하다.

### [활동] DataFrame을 사용한 단어 수

#### Using SQL Functions

- `pyspark.sql.functions`를 import하여 SQL function을 사용해보자.
  
  - `functions as func`로 사용하겠다 ;;

- `func.explode()` - 기본적으로 `flatmap`과 동일함.

- `func.split()`, `func.lower()`

#### DataFrames work best with Structured data

- `dataframe`은 **정형화된 데이터**에 적합(fit)하다.

- 한줄 한줄로 이뤄진 도서 텍스트 데이터의 경우 `RDD`가 적합할 수 있다.
  
  - 상황에 맞게 조합하여 사용하자!

#### 데이터에서 단어 수를 count

- 이런 형태의 데이터는 어떻게 처리해야 할까?
  
  ![2023-01-12-01-24-26-image](https://user-images.githubusercontent.com/81341784/211872115-10fed075-30ad-4f4d-ae75-df359913312a.png)아마 `RDD`의 형태가 적절할거다. 한줄은 1개의 row로 치환되며, 1개의 row는 1개의 column을 갖는다.
  
  1개 컬럼에는 1줄의 모든 텍스트가 담길거다.
  
  해당 데이터에 단어 수를 count해보자

- 데이터를 불러와 `explode`를 통해 flatmap을 수행한다. `\\W+` 를 기준으로 `split`하는 함수를 적용한다.
  
  ![2023-01-12-01-28-03-image](https://user-images.githubusercontent.com/81341784/211872202-c39589bd-6865-48b6-b458-c4d1943ed98c.png)`alias`를 통해 컬럼의 이름을 "word"로 명시해줬다.

- 분할한 단어들을 `lower`을 통해 소문자로 Nomalize해주고
  
  ![2023-01-12-01-32-41-image](https://user-images.githubusercontent.com/81341784/211872232-4d95cd61-90ae-4a99-b783-ecca90184f22.png)"word"를 기준으로 `groupby`한 후 count한다.

- 단어별로 groupby하여 count한후, count 값에 따라 sort한 결과를 확인할 수 있다.
  
  ![2023-01-12-01-34-41-image](https://user-images.githubusercontent.com/81341784/211872268-1933854a-8b00-452e-97b9-b1e6d7d4ecef.png)
  
  ### [활동] DataFrame의 최소 온도(커스텀 스키마 활용)

- `withColumn`을 통해 데이터 프레임에 새로운 컬럼을 추가해보자.

- ```python
  from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
  schema = StructType([ \
                     StructField("stationID", StringType(), True), \
                     StructField("date", IntegerType(), True), \
                     StructField("measure_type", StringType(), True), \
                     StructField("temperature", FloatType(), True)])
  df = spark.read.schema(schema).csv("file:///SparkCourse/1800.csv")
  df.printSchema()
  ```
  
  위 예시와 같이 `StructType`과 `StructField`를 활용하여 새로운 스키마를 정의할 수 있다.
  
  정의 스키마를 데이터를 불러올때 옵션으로 사용 가능하다.

- 그 이후는 이전에 했던것 처럼, 필요 데이터로 새로운 테이블을 생성하고
  
  ![2023-01-12-01-46-57-image](https://user-images.githubusercontent.com/81341784/211872337-176392cb-9d72-41df-aec2-d158f6d20efb.png)화씨 온도인 최소 온도(temperature)를 섭씨로 바꿔준 값을 `withColumn`함수로 변환해준다.
  
  ![2023-01-12-01-48-30-image](https://user-images.githubusercontent.com/81341784/211872387-057b653f-24e2-4693-b51b-d6199e5dd1d5.png)

--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
