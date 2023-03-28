- TOC

# Java_05

## 배열

- **같은 타입**의 여러 변수를 하나의 묶음으로 다루는 것

```java
int[] score = new int[5]; // 5개의 int값을 저장할 수 있는 배열 생성
```

### 배열의 선언과 생성

```java
타입[] 변수이름; // 배열을 선언
변수이름 = new 타입[길이]; // 배열을 생성

int [] score; // int타입의 배열을 다루기 위한 참조변수 score 선언
score = new int[5]; // int타입의 값을 5개를 저장할 수 있는 배열 생
```

- 인덱스는 0부터 시작..

- `arr.length();`로 배열의 길이 반환가능.

#### 배열의 초기화

- 배열은 생성과 동시에 자동적으로 기본값(0)으로 초기화된다.

- 필요에 의한 값을 저장해줘야 한다.

- 일일히 저장해줄 수 있지만

```java
int[] score = new int[]{50, 60, 70, 80, 90}
int[] score = new int[]{50, 60, 70, 80, 90} // new int[] 생략가능
```

- 위와 같이 초기화 가능하다.

#### 배열의 출력

- for문을 통해 배열의 각 인자에 접근하여 출력하는 방법도 있지만,

- `toString`을 사용하면 `[인자1, 인자2....]`의 형식으로 출력가능하다.

- `Arrays.toString()`을 사용하려면 `import java.utill.Arrays;`를 추가해야한다.

```java
int[] iArr = {100, 95, 80, 70, 60};
System.out.println(Arrays.toString(iArr));
```

- 위 `iArr`배열을 그대로 출력하면 "타입@주소"가 출력하여 볼게없다.

- char 배열을 그대로 출력시 각 요소가 구분자없이 출력된다.

```java
char[] chArr = {'a','b','c','d'};
System.out.println(chArr) // abcd 출
```

#### 배열의 활용

- 총합, 평균, 최대-최솟값, 배열 요소 섞기...etc..

#### String배열의 선언과 생성

- 배열의 타입이 String인 경우에도  int배열의 선언과 생성방법은 다르지 않다.
  
  `String[] name = new String[3];` 3개의 문자열을 담는 배열을 생성한다. 기본값은 `null`을 갖는다. 

#### String클래스의 주요 메서드

| 메서드                                | 설명                         |
| ---------------------------------- | -------------------------- |
| char charAt(int index)             | 문자열에서 해당 인덱스의 문자 반환        |
| int length()                       |                            |
| String substring(int from, int to) | 문자열에서 해당 범위의 문자열 반환        |
| boolean equals(Object obj)         | 문자열의 내용이 같은지 boolean 반환    |
| char[] toCharArray()               | 문자열을 문자배열(char[])로 변환하여 반환 |

#### 2차원 배열의 선언

```java
타입[][] 변수이름; 타입 변수이름[][]; 타입[] 변수이름[];ㄴㅇㄹㄴㅇ
```

- `int[][] score = new int[4][3];`4행 3열의 2차원 배열 생성

#### 2차원 배열의 초기화

- 1차원 배열과 같은 중괄호를 통해 생성과 초기화를 동시에 가능

```java
int[][] arr = new int[][]{ {1,2,3}, {4,5,6}};
int[][] arr = {{1,2,3}, {4,5,6}}; 
```

### Arrays로 배열다루기

#### 배열의 비교와 출력

- 일차원 배열에서는 `equals()`와 `toString()`이 작동하지만, 다차원 배열은 깊은 적용이 안된다.

- `deepToString()`을 통한 배열의 모든 요소를 문자열 변환

- `deepEquals()`를 사용하여 다차원 배열 비교

#### 배열의 복사

- `copyOf(arr, int to)`로 배열 전체를
- `copyOfRange(arr, int from, int to)`로 배열의 일부를 복사하여 새로운 배열을 반환

#### 배열의 정렬

- `sort(Array arr)`을 사용한다.

# 
