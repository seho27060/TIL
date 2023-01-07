[TOC]

# Spark-with-Python 02

## Spark 기본 사항 및 RDD 인터페이스

### 위치별 RDD 및 최소 온도 필터링

- RDD의 `filter`를 사용해보자.

- `filter` - 불필요한 정보를 제거하여 데이터하는 연산
  
  ```python
  minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
  ```
  
  `x[1]`에 `"TMIN"`이 있는 데이터만 반환한다.

#### 워크스루

- 스파크 컨텍스트 설정 및 sc 객체 생성
  
  ```python
  conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
  sc = SparkContext(conf = conf)
  ```

- 데이터를 불러와 사용자 정의 메서드 `parseLine`으로 RDD의 모든 라인(단위 데이터)에 적용한다.
  
  ```python
  lines = sc.textFile("file:///SparkCourse/1800.csv")
  parsedLines = lines.map(parseLine)
  
  def parseLine(line):
      fields = line.split(',')
      stationID = fields[0]
      entryType = fields[2]
      temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
      return (stationID, entryType, temperature)
  ```
  
  반점 `,`로 구분된 데이터를 나누고 각 값을 할당한다. `temperature`의 경우 섭씨 온도를 화씨로 변환하는 과정이다.

- `entryType`이 "TMIN"인 데이터를 필터링하고
  
  ```python
  minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
  stationTemps = minTemps.map(lambda x: (x[0], x[2]))
  ```
  
  사용한 `entryType`은 필요없으므로 해당 컬럼을 제외한 RDD를 생성한다.

- `reduceByKey`를 통해 가장 작은 값을 찾는다.(`min(x,y)`함수 사용)
  
  ```python
  minTemps = stationTemps.reduceByKey(lambda x, y: min(x,y))
  results = minTemps.collect();
  ```
  
  `collect`로 결과를 파이썬 List로 반환한다.

### Flatmap()을 이요한 단어 발생 횟수 세기

#### map() vs flatmap()

- map() : RDD의 각 원소를 새 원소로 변환해준다.
  
  - 기존 RDD와 새로운 RDD간의 일대일 대응이 성립한다.

- flatmap() : RDD의 원소를 여러 항목으로 나눈다.
  
  - 기존 RDD와 일대일 대응이 안될 수 있다.
  
  - EX) 4줄의 RDD에 `flatmap`을 통해 `split`함수로 분할하면,, 4줄의 RDD가 아닌 각 단어 별로 나눠어 각각의 항목을 갖는 RDD로 변환된다.

- `map`은 변환 이전/이후 RDD의 크기가 invariant하지만, `flatmap`은 아닐 수 있다

#### Count the words in a book

- 스파크 컨택스트 설정, 객체 생성하고

- 데이터를 불러온다.

- `flatmap`을 활용하여 `split`을 적용하여 줄로 구성된 데이터를 단어별로 분할한다.
  
  ```python
  input = sc.textFile("file:///sparkcourse/book.txt")
  words = input.flatMap(lambda x: x.split())
  wordCounts = words.countByValue()
  ```
  
  분할된 단어를 값(단어)별로 갯수를 센다

- 와우 그런데 공백으로 나누다 보니 불용어가 많이 포함되어 있다.

- 단어별로 count 한 값을 내림차순으로 보고싶기도 한데 말이야..

### 정규표현식으로 단어 수 스크립트 개선하기

- 간단한 아이디어다. 정규표현식으로 불용어를 제거하여 단어 정제하기

- `normalizeWords` 메서드를 생성하여 라인별로 단어를 분할하고 불용어를 정제한다.
  
  ```python
  input = sc.textFile("file:///sparkcourse/book.txt")
  words = input.flatMap(normalizeWords)
  wordCounts = words.countByValue()
  
  def normalizeWords(text):
      return re.compile(r'\W+', re.UNICODE).split(text.lower())
  ```

- 굳 ".",",","/"등과 같은 기호 및 불용어가 정리되니 보기 편하다

- 근데 단어 빈도별로 출력할 순 없을까?

### 단어 개수 결과 정렬하기

- 약간의 수정이 필요하다

- `map`으로 단어로  `flatmap`된 RDD들을 (단어, 1) 형식으로 바꾼뒤, `reduceByKey`를 활용하여 (단어,1)의 1 값을 차근차근 더해간다
  
  ```python
  wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y) 
  ```

- 이제 (단어, 1) 에서 (단어, 단어갯수)의 형식으로 변환되었고, 다시 (단어갯수, 단어) 순서로 뒤바꾼 후 단어 갯수 대로 정렬한다.
  
  ```python
  wordCountsSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey()
  ```





- 함수형 프로그래밍이라더니..`lambda`만 음청 사용하네..



--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
