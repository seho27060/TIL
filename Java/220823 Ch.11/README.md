# Java_11

## 컬렉션 프레임워크

- 데이터 군을 저장하는 클래스들을 표준화한 설계

### 컬렉션 프레임워크의 핵심 인터페이스

- Collection = List + Set

- Map

### List

- 순서가 있는 데이터 집합, 데이터의 중복 허용

- ArrayList, LinkedList, Stack, Vector...etc

#### ArrayList

- 기존의 Vector를 개선한 것

- 배열을 순서대로 저장하며, 더 이상 저장할 공간이 없으면 보다 큰 새로운 배열을 생성해서 기존의 배열에 저장된 내용을 새로운 배열로 복사한다.

- 추가와 삭제에 있어 중간 요소를 삭제할 경우 다른 데이터들의 위치를 이동시켜 덮어쓰는 과정이기 때문에 작업시간이 오래걸린다.

- Stack 적합

#### LinkedList

- 배열의 크기 변경 불가, 비순차적 데이터의 추가 삭제의 작업시간이 오래걸림 등의 단점을 보완하기 위한 자료구조

- 모든 요소가 불연속적으로 존재하고, 데이터를 서로 연결(link)한 형태로 구성

```java
class Node {
 Node next; // 다음 요소의 주소
 Object obj; // 데이터를 저장
 }
```

- 추가와 삭제에 있어서 배열처럼 데이터를 복사-이동하는 과정이 없기 때문에 처리속도가 매우 빠르다.

- 추가 삭제에 엤어서 `Node`의 다음 요소의 주소만 수정해주면 된다.

- 배열은 정해진 주소를 통한 접근이 빠르지만, 링크드리스트의 경우 특정 요소에 접근하기 위해 처음부터 특정요소까지 차례대로 접근해야하기 때문에 데이터 접근이 비교적 느리다.

- Queue 적합

### Iterator, Listiterator, Enumeration

- 컬렉션에 저장된 요소를 접근하는데 사용되는 인터페이스

- iterator : 컬렉션에 저장된 요소를 접근하는데 사용되는 인터페이스

- LIstiterator : iterator에 양방향 조회 기능 추가(List를 구현한 경우만 사용가능)

- Enumeration : iterator의 구버전

```java
public interface Iterator{
    boolean hasNext();
    Object next();
    void remove();
}
```

- `iterator()` 구현 내용

```java
List list = new ArrayList();
Iterator it = list.iterator();


while(it.hadNext()){ // boolean hasNext() 읽어올 다음 요소가 있는 확인
    System.out.println(it.next());  // Object next() 다음 요소를 읽어
```

#### Map과 Iterator

- Map 인터페이스로 구현한 클래스는 키와 값을 쌍으로 저장하고 있기 때문에 iterator()를 직접 호출할 수 없고, 그 대신  keySet()이나 entrySet()과 같은 메서드를 통해서 키와 값을 각각 따로 Set의 형태로 얻어온 후에 다시 iterator()를 호출해야한다.

```java
Map map = new HashMap();
...
Iterator it = map.entrySet().iterator();
```

#### Array의 메서드

- 복사 - copyOf(), copyOfRange()

- 배열 채우기 - fill(), setAll()

```java
int[] arr = new int[5];
Arrays.fill(Arr, 9); // arr =[9,9,9,9,9]
Arrays.setAll(arr,(i) -> (int)(Math.random()*5)+1); // arr=[random값 5개]
```

- 정렬과 검색 - sort(), binarySearch()

```java
int[] arr = {3,2,0,1,4};
Arrays.sort(arr); // arr 정렬, [0,1,2,3,4]
int idx = Arrays.binarySearch(arr,2); // idx =2 반환, 올바른 결과
```

- 문자열의 비교와 출력 - equals(), toString()
- 배열을 List로 변환 - asList(Object...a) 
  
  ```java
  List list = Arrays.asList(new Integer[]{1,2,3,4,5});
  list.add(6); // UnsupportedOperationException 예외 발생
  ```
- asList()가 반환한 List의 크기는 변경할 수 없다.

#### Comparator 와 Comparable

- 인터페이스로 컬렉션을 정렬하는데 필요한 메서드 정의]

- `sort()`와 같은 정렬에서 Comparator을 지정하여 원하는 대로 정렬한다.

```java
static void sort(Object[] a) // 객체 배열에 저장된 객체가 구현한 Comparable에 의한 정렬
static void sort(Object[] a, Comparator c) // 지정한 Comparator에 의한 정렬
```

### Set

- 순서를 유지하지 않는 데이터의 집합, 데이터의 중복 허용하지 않음

- HashSet, TreeSet

#### HashSet

- Set 인터페이스를 구현한 대표적 컬렉션

- 중복 허용 X, 순서 보장 X

- 순서 보장을 위해 LinkedHashSet을 사용해야한다.

- `add()`나 `addAll()`메서드를 통해 새로운 요소가 추가되는데, 이때 이미 저장되어 있는 요소라면 메서드는 `false`를 반환하고 추가에 실패한다.

#### TreeSet

- **이진 탐색 트리(binary search tree)** 라는 자료구조의 형태로 데이터를 저장하는 컬렉션 클래스

- 중복된 데이터 허용 X, 정렬된 위치에 저장하므로 저장순서 유지하지 않음.

```java
class TreeNode{
    TreeNode left; // 왼쪽 자식 노드
    Object element; // 객체를 저장하기 위한 참조변수
    TreeNode right; // 오른쪽 자식 노드
}
```

### Map

- 키(key)와 값(value)의 쌍으로 이뤄진 데이터의 집합

- 순서는 유지되지 않으며, 키는 중복을 허용하지 않고 값은 중복이 허용

- HashMap, TreeMap, Hashtable, Properties

#### HashMap 과 Hashtable

- Hashtable과 HashMap의 관계는 Vectro와 ArrayList의 관계와 같아서 Hashtable보다는 HashMap을 사용할 것을 권한다.

### Collections의 메서드

#### 동기화

- 멀티 쓰레드(multi - thread) 프로그래밍에서는 하나의 객체를 여러 쓰레드가 동시에 접근 할 수 있기 때문에, 데이터의 무결성을 유지하기 위해서는 공유되는 객체에 동기화(synchronization)가 필요하다.

```java
List syncList = Collections.synchronizedList(new ArrayList(...));
```

#### 변경불가, 싱글톤

- 변경불가 컬렉션 : 컬렉션에 저장된 데이터를 보호하기 위해, 읽기전용으로 만들때, 멀티 쓰레드 프로그래밍에서 여러 쓰레드가 하나의 컬렉션을 공유하다보면 데이터가 손상될 수 있는데, 이를 방지하려면 아래의 메서드들을 이용하자.

```java
static Collection unmodifableCollection(Collection c)
```

- `unmodifiable`을 붙여주자

- 싱글톤 컬렉션 : 단 하나의 객체만을 저장하는 컬렉션을 만들어야 하는 경우

```java
static List singletonList(Object o)
static Set singleton(Object o)
static Map singletonMap(Object key, Object value)
```

#### 단일 컬렉션

-  컬렉션에 모든 종류의 객체를 저장할 수 있다는 것은 장점이기도 하고 단점이기도 하다.

- 대부분 한 종류의 객체를 저장하며, 컬렉션에 지정된 종류의 객체만 저장하고 싶을때는 아래의 메서드를 사용한다.

```java
static Collection checkedCollection(Collection c, Class type)
```

- `checked`를 붙여주고, 원하는 종류의 `class`를 지정해준다.

```java
List list = new ArrayList();
List checkedList = checkedList(list, String.class); //String만 저장가능
checkedList.add("abc");
checkedList.add(new Integer(3)); // ClassCastException 에러 발생
```
