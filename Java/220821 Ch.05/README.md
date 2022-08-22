[TOC]

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

# Java_06

## 객체지향 프로그래밍 I

- 객체지향언어의 주요 특징
  
  1. 코드의 높은 재사용성
  
  2. 코드의 관리 용이
  
  3. 신뢰성이 높은 프로그래밍 가능

#### 클래스와 객체

- 클래스 : 객체를 정의해 놓은 것/ 객체를 생성하는데 사용한다.

- 객체 : 실제로 존재하는것, 클래스에 정의된 내용대로 메모리에 생성된 것

#### 객체의 구성 요소 - 속성과 기능

- 속성(property) : 멤버변수(variable)

- 기능(function) : 메서드(method)

#### 객체와 인스턴스

- 인스턴스화(instantiate):클래스로부터 객체를 만드는 과정.

- 인스턴스(instance): 클래스로부터 만들어진 객체

### 한 파일에 여러 클래스 작성하기

- 하나의 소스파일에 하나의 클래스만을 정의하는 것이 보통.

- 하나의 소스파일에 둘 이상의 클래스 정의도 가능하다.

- 이때 주의할 점은 '소스파일의 이름은 public class의 이름과 일치해야한다'

```java
// Hello2.java
public class Hello2 {}
       class Hello3 {}// 이렇게 작성해야한다. 
```

### 객체의 생성과 사용

```java
클래스명 변수명; // 클래스의 객체를 참조하기 위한 참조변수 선언
변수명 = new 클래스명(); // 클래스의 객체 생성후, 객체의 주소를 참조변수에 저장


Tv = t;
t = new Tv();
```

- 실사용 예

```java
class Ex6_1 { 
    public static void main(String args[]) { 
        Tv t;                 // 참조변수 선      
        t = new Tv();         // 참조변수에 인스턴스 생성
        t.channel = 7;        // 인스턴스의 멤버변수에 값 할
        t.channelDown();      // 인스턴스의 메서드 호 
        System.out.println("현재 채널 " + t.channel + " 입니다."); 
    } 
}

// 클래스 Tv 선언.
class Tv { 
    // Tv의 속성   
    String color;           //  
    boolean power;             // 
    int channel;               // 

    // Tv의 기능
    void power()   { power = !power; }  // 
    void channelUp()   {  ++channel; }  // 
    void channelDown() { --channel; }   //
}
```

- 인스턴스는 참조변수를 통해서만 다룰수 있으며, 참조변수의 타입은 인스턴스의 타입과일치해야 한다.

- `Tv t1 = new Tv();`, `Tv t2 = new TV();`와 같이 t1, t2 두개의 같은 클래스를 갖는 서로 다른 인스턴스를 생성하였다. 서로 다른 값을 유지할 수 있으며. 메서드의 내용은 동일하다.

### 객체배열

- 객체로 이루어진 배열을 '객체배열' 이라한다.

```java
Tv tv1, tv2, tv3; -> Tv[] tvArr = new Tv[3];
```

- `Tv`클래스를 요소로 갖는 3의 길이를 갖는 배열 생성.

### 클래스의 정의

#### 데이터와 함수의 결합

- '객체를 생성하기 위한 틀' 이란 정의는 객체지향이론의 관점에서 클래스 정의

- 서로 관련된 변수들을 정의하고 이들에 대한 작업을 수행하는 함수들을 함께 정의한 것이 프로그래밍적인 관점에서의 클래스 정의

#### 사용자 정의 타입

- 기본 자료형(primitive type) 외 서로 관련된 변수들을 묶어서 하나의 타입으로 추가하는 것을 '사용자정의 타입(user-defined type)'이라고 한다.

```java
class Time {
    int hour;
    int minute;
    float second;
}
```

### 선언위치에 따른 변수의 종류

- 변수는 클래스 변수, 인스턴스 변수, 지역변수 모두 세 종류가 있다.

```java
class Variables{
    int iv; // 인스턴스 변수
    static int cv; // 클래수 변수(static 변수, 공유 변수

    void method(){
    int lv = 0; // 지역 변수
}
}
```

| 변수의 종류  | 선언위치                                 | 생성시기            |
| ------- | ------------------------------------ | --------------- |
| 클래스 변수  | 클래스 영역                               | 클래스가 메모리에 올라갈 때 |
| 인스턴스 변수 |                                      | 인스턴스가 생성되었을 때   |
| 지역 변수   | 클래스 이외의 영역<br/>(생성자, 메서드, 초기화 블럭 내부) | 변수 선언문이 수행되었을때  |

- 클래스 변수 : 하나의 클래스에 대해 공통된 저장 공간을 공유하는 변수(하나의 클래스로 생성된 모든 인스턴스가 공통된 값을 갖음)

- 인스턴스 변수 : 인스턴스가 생성될때마다 만들어진다. 객 인스턴스마다 고유의 값을 갖는다.

- 지역 변수 : 메서드 내에 선언되어 메서드 내에서만 사용가능한 값.

### 메서드란?

- 메서드(method) : 특정 작업을 수행하는 일련의 문장들을 하나로 묶은것.

```java
반환타입 메서드이름(타입 변수명, 타입 변수명,...){
    // 메서드 호출시 수행될 코
}
```

- 반환타입 : void로 할경우 return 필요없음, 그외는 return 필요함

#### 호출스택(call stack)

- 메서드의 작업에 필요한 메모리 공간을 제공한다.

```java
class Ex6_5 {
    public static void main(String[] args) {
        System.out.println("Hello");        
    }
}
```

1. main 이 스택에 쌓인다.

2. main안의 println이 쌓인다.

3. println의 동작이 마무리되면 호출 스택에서 사라진다.

4. main의 내용도 끝나면 호출 스택에서 사라진다.

5. 호출 스택이 비워지고 프로그램은 종료.

#### 기본형 매개변수 & 참조형 매개변수

- 메서드를 호출할 때 매개변수로 지정한 값을 메서드의 매개변수에 복사해서 넘겨준다.

- 매개변수의 타입이 기본형일때는 기본형 값이 복사되고, 참조형일때는 인스턴스의 주소가 복사된다.

```java
class Data { int x; }

class Ex6_7 {
    public static void main(String[] args) {
        Data d = new Data();
        d.x = 10;
        System.out.println("main() : x = " + d.x);

        change(d.x);
        System.out.println("After change(d.x)");
        System.out.println("main() : x = " + d.x);
        change2(d);
        System.out.println("After change2(d.x)");
        System.out.println("main() : x = "+d.x);
        }

        static void change(int x) {  // 기본형 매개변
            x = 1000;
            System.out.println("change() : x = " + x);
        }    
        static void change2(Data d) { // 참조형 매개변
            d.x = 1000;
            System.out.println("change2() : x = " + d.x);
        }
    }
```

- 메서드를 통해 인스턴스의 값(참조형 매개변수)를 변경할 수도 있다.

#### 참조형 반환 타입

- 반환타입또한 참조형이 될수 있다.

- 모든 참조형 타입의 값은 '객체의 주소' 이므로 그저 정수값이 반환되는 것일 뿐 특별할 것이 없다.

### static 메서드와 인스턴스 메서드

- 변수에서와 같이 메서드 앞에 static이 붙으면 클래스 메서드, 아니면 인스턴스 메서드이다.

- 클래스 메서드는 객체를 생성하지 않고도 사용 가능한것에 비해

- 인스턴스 메서드는 반드시 객체를 생성해야만 호출 가능하다.

#### static을 언제 붙여야 할까?

1. 클래스를 설계할때, 멤버 변수 중 모든 인스턴스에 공통으로 사용하는 경우

2. 클래스 변수는 인스턴스를 생성하지 않아도 사용 할 수 있다.

3. 클래스 메서드는 인스턴스 변수를 사용할 수 없다./ 인스턴스 메서드나 변수는 static이 붙은 멤버들을 언제든 사용가능 하다.

4. 메서드 내에서 인스턴스 변수를 사용하지 않는다면, static을 붙이는 것을 고려한다.

#### 메서드 간의 호출과 참조

- 같은 클래스에 속한 멤버들 간에는 별도의 인스턴스 생성없이 참조, 호출이 가능하다.

- 단, 클래스멤버가 인스턴스 멤버를 참조 또는 호출하고자 하는 경우에는 인스턴스를 생성해야 한다.

- **인스턴스 멤버가 존재하는 시점에 클래스 멤버는 항상 존재하지만, 클래스 멤버가 존재하는 시점에 인스턴스 멤버가 존재하지 않을 수도 있기 때문이다.**

#### 오버로딩(overloading)

- 메서드 오버로딩(method overloading) : 한 클래스 내에 같은 이름의 메서드를 여러 개 정의하는 것.

- 아래와 같은 조건을 만족해야한다.
  
  1. 메서드 이름이 같고
  
  2. 매개변수의 개수 또는 타입이 달라야 하며,
  
  3. 반환 타입은 관계없다.

- 매개변수의 타입 | 개수가 다르면 오버로딩이 성립한다고 보면된다.

#### 생성자(constructor)

- 인스턴스가 생성될 때 호출되는 '인스턴스 초기화 메서드'이다.

- 다음 조건을 따른다.
  
  1. 생성자의 이름은 클래스의 이름과 같아야 한다.
  
  2. 생성자는 리턴 값이 없다.

```java
클래스이름(타입 변수명, 타입 변수명,...){
    // 인스턴스 생성 시 수행될 코드,
    // 주로 인스턴스 변수의 초기화 코드를 적는다.
}
```

- 생성자도 오버로딩이 가능하다.

#### 기본 생성자(default constructor)

- java에서는 클래스에 생성자가 하나도 정의되지 않은 경우, 컴파일러가 자동으로 기본 생성자를 추가하여 컴파일한다.

```java
class Data_1 {
    int value;
}

class Data_2 {
    int value;

    Data_2(int x) {   // 매개변수가 있는 생성자.
        value = x;
    }
}

class Ex6_11 {
    public static void main(String[] args) {
        Data_1 d1 = new Data_1();
        Data_2 d2 = new Data_2(); // compile error발생
    }
}
```

- `Data_2 d2 = new Data_2();`에서 생성자가 선언되었지만, 매개변수가 없을때의 생성자는 선언되지 않아 에러가 발생한다.

- 매개변수가 있는 생성자를 선언하였으므로, 인스턴스 생성시 매개변수를 담아 생성하면 에러가 발생하지 않는다.

#### 생성자에서 다른 생성자 호출하기 - this()

- 같은 클래스의 멤버들 간에 서로 호출할 수 있는 거 처럼, 생성자 간에도 서로 호출이 가능하다. 다음 두 조건을 만족해야 한다.
  
  1. 생성자의 이름으로 클래스이름 대신 this를 사용한다.
  
  2. 한 생성자에서 다른 생성자를 호출할 때는 반드시 첫 줄에서만 호출이 가능하다.

```java
class Car2 {
    String color;        
    String gearType;    
    int door;            

    Car2() {
        // color = 'white';
        // gearType = "auto";
        // door = 4; 를 아래와 같이 간결하게 표현 가능하다.
        this("white", "auto", 4);
    }

    Car2(String color) {
        this(color, "auto", 4);
    }

    Car2(String color, String gearType, int door) {
        this.color = color;
        this.gearType = gearType;
        this.door = door;
    }
}
class Ex6_13 {
    public static void main(String[] args) {
        Car2 c1 = new Car2();    
        Car2 c2 = new Car2("blue");

        System.out.println("c1�� color=" + c1.color + ", gearType=" + c1.gearType+ ", door="+c1.door);
        System.out.println("c2�� color=" + c2.color + ", gearType=" + c2.gearType+ ", door="+c2.door);
    }
}
```

#### 객체 자신을 가리키는 참조변수 - this

- 'this'는 참조변수로 인스턴스 자신을 가리킨다. 인스턴스의 주소가 저장되어 있다. 모든 인스턴스메서드에 지역변수로 숨겨진 채로 존재한다.

```java
Car(String c, String g, int d) {
    color = c;
    gearType = g;
    door = d;
}

///

Car(String color, String gearType, int door){
    this.color = color;
    this.gearType = gearType;
    this.door = door;
}
```

- 인스턴스 변수 ` this.color`에 생성자의 매개변수로 정의된 지역변수 `color`를 할당한다. `this`로 구분한다.

- `this`와 `this()`는 **전혀 다른 것**이다. `this`는 참조 변수이고, `this()`는 생성자이다.

#### 변수의 초기화

- 선택이지만, 가능하면 선언과 동시에 적절한 값으로 초기화하는게 바람직하다.

- **지역변수는 사용하기 전에 반드시 초기화해야 한다.**

- 인스턴스 변수는 자동으로 초기화 되지만, 지역변수는 그렇지 않기 때문이다.

# 
