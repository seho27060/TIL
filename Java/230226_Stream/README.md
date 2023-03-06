- [Java](#java)
  - [Stream](#stream)
      - [특징](#특징)
    - [`Stream` 생성하기](#stream-생성하기)
    - [`Stream` 가공하기](#stream-가공하기)
      - [`map()`](#map)
      - [`filter()`](#filter)
      - [`collect()`](#collect)

---

# Java

## Stream

> `Collection`, 배열에 저장된 요소들을 하나씩 참조하여 반복적인 처리를 하는 `API`

- `stream`는 `Java8` 부터 지원되는 `API`로 배열과 같은 데이터에 조건에 따른 처리 후 반환하는 작업에 사용할 수 있다.

- `Java8` 이전에는 `collection`, 배열 인스턴스를 다루기 위해 `for`나 `foreach`를 통해 요소를 하나씩 꺼내 사용했다. 
  
  - `stream`을 통해 코드의 양이 간결해지고 생산성을 높일 수 있게 되었다.

#### 특징

- `stream`은 원본 데이터를 **읽기**만 하지, 원본데이터 변경을 하지 않는다.

- 정렬 결과를 `collection`이나 배열에 담아 반환할 수 있다.

- 내부 반복문으로, 반복문이 코드상에 노출되지 않는다.

### `Stream` 생성하기

- 배열 스트림 생성
  
  ```java
  String[] array = new String[]{"a","b","c"};
  Stream<String> stream = Arrays.stream(array); // 배열array 전체를 Stream으로 생성
  Stream<String> streamOfArray = Arrays.stream(array,1,3); // 배열 array의 부분을 Stream으로 생성
  ```

- 컬렉션 타입(`Collection`, `List`, `Set`) 스트림 생성
  
  ```java
  List<String> list = Arrays.asList("x","y","z");
  Stream<String> stream = list.stream();
  Stream<String> parallelStream = list.parallelStream(); // 병렬 처리 스트림
  ```

### `Stream` 가공하기

#### `map()`

- 배열의 요소들을 **조건에 맞게** 변환한다.
  
  ```java
  List<String> list = new ArrayList<>(Arrays.asList("one","two","three"));
  
  Stream result1 = list.stream().map(o -> o.toUpperCase()); // ONE TWO THREE 로 반환
  ```

#### `filter()`

- `Stream`내의 요소에 대해 **필터링**한 값을 반환한다.
  
  ```java
     Stream result2 = list.stream().filter(o -> o.length() < 3); // 길이가 3보다 작은 one, two 반환
  Stream result3 = list.stream().filter(o -> o.startWith("s")); // s 로 시작하는 문자열 반환 
  ```

#### `collect()`

- `Stream` 데이터를 **원하는 자료형**으로 변환하여 반환한다.
  
  ```java
  Long count = list.stream().filter(o -> o.length() < 3).collect(counting());   // 길이가 3보다 작은 문자열은 2개이므로 2 반환
  
  List filteredList = list.stream().filter(o -> o.startWith("t")).collect(Collectors.toList()); 
  // "t"로 시작하는 문자열 two, three를 List 형태로 반환한다.
  
  Map map = list.stream().filter(o -> o.length() < 3).collect(Collectors.toMap(a -> a, a -> a.length()); 
  // 길이가 3보다 작은 요소를 요소값 : 요소의 길이의 key-value 형식의 Map 형태로 반환한다.
  ```

---

- 레퍼런스

> https://futurecreator.github.io/2018/08/26/java-8-streams
> [java8 stream의 쉬운 사용방법 (map, filter, collect)](https://www.appletong.com/entry/java8-stream-%EC%82%AC%EC%9A%A9%EB%B0%A9%EB%B2%95-map-filter-collect)https://codechacha.com/ko/java8-stream-collect/
